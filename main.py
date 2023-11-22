from redis_db.redis_service import *
from utils.ws_interface import *
from constants import *
global random_ids_list


if __name__ == "__main__":
    load_dotenv(".env")

    result_redis = RedisHash(port=getenv("REDIS_PORT"),db_id=getenv("results_redis"), key_field="ItemId",expiry_time=66000)
    markets_redis = RedisHash(port=getenv("REDIS_PORT"),db_id=getenv("markets_redis"), key_field="ItemId",expiry_time=66000)
    miss_ids_redis = RedisHash(port=getenv("REDIS_PORT"),db_id=getenv("missing_ids_redis"),expiry_time=66000)
    ws=WebsocketClient(ws_url=getenv("ws_url"),miss_keys_redis=miss_ids_redis,markets_redis=markets_redis,result_redis=result_redis)
    ws.connection()

