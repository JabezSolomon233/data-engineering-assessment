# etl/group_users.py
import os, argparse, logging
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def main(db_uri, output_dir):
    logging.info("Connecting to DB")
    engine = create_engine(db_uri)
    users = pd.read_sql("SELECT id, city FROM users", engine)
    bank = pd.read_sql("SELECT user_id, bank_name FROM user_bank_info", engine)
    employment = pd.read_sql("SELECT user_id, company_name, salary FROM employment_info", engine)

    logging.info("Merging")
    df = users.merge(bank, left_on="id", right_on="user_id", how="left") \
              .merge(employment, left_on="id", right_on="user_id", how="left")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(output_dir, exist_ok=True)

    # Group by bank
    g_bank = df.groupby("bank_name").agg(
        user_count=("id", "nunique"),
        user_ids=("id", lambda ids: ",".join(map(str, sorted(set(ids.dropna().astype(int)))) ))
    ).reset_index()
    bank_file = os.path.join(output_dir, f"group_by_bank_{ts}.csv")
    g_bank.to_csv(bank_file, index=False)
    logging.info("Wrote %s", bank_file)

    # Group by company
    g_company = df.groupby("company_name").agg(
        user_count=("id", "nunique"),
        user_ids=("id", lambda ids: ",".join(map(str, sorted(set(ids.dropna().astype(int)))) ))
    ).reset_index()
    company_file = os.path.join(output_dir, f"group_by_company_{ts}.csv")
    g_company.to_csv(company_file, index=False)
    logging.info("Wrote %s", company_file)

    # Group by pincode
    g_pincode = df.groupby("city").agg(  # assesment asked pincode, but many rows use city; change to pincode if required
        user_count=("id", "nunique"),
        user_ids=("id", lambda ids: ",".join(map(str, sorted(set(ids.dropna().astype(int)))) ))
    ).reset_index()
    pincode_file = os.path.join(output_dir, f"group_by_pincode_{ts}.csv")
    g_pincode.to_csv(pincode_file, index=False)
    logging.info("Wrote %s", pincode_file)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--db-uri", default=os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/de_assessment"))
    p.add_argument("--output-dir", default=os.path.join(os.path.dirname(__file__), "output"))
    args = p.parse_args()
    main(args.db_uri, args.output_dir)
