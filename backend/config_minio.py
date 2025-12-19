
import boto3
# ---------------- MINIO ----------------
MINIO_ENDPOINT ='http://10.161.67.41:9000'# 'http://minio:9000'#'http://10.161.67.41:9000'##'http://127.0.0.1:9000'# 'http://minio:9000'#'http://127.0.0.1:9000'
ACCESS_KEY = 'admin_minio'
SECRET_KEY = 'admin_minio'
BUCKET_NAME = 'ehskunshan'


# ---------------- sql server ----------------

META_COLUMNS = {'object_name':'object_name',
        'product_name':'product_name',
        'linespeed_spec':'linespeed_spec',
        'linespeed_real':'linespeed_real',
        'production_line':'production_line',
        'cameraid':'cameraid',
        'photo2check_bool':'photo2check_bool',
        'photo2minio_status':'photo2minio_status',
        'productnameid':'productnameid',
        'createtime_utc':'createtime_utc'
 }



s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=boto3.session.Config(proxies={})  # 不使用代理
    # 如果使用 https，需要设置 verify=True
)

