# coding=utf8
from DBUtils.PooledDB import PooledDB
import MySQLdb
from MySQLdb.cursors import DictCursor
import threading
import logging
import traceback
from flask import Flask

app = Flask(__name__)
from decimal import Decimal


def dict_decimal_to_float(d):
    if not isinstance(d, dict):
        raise TypeError("d must be dict")
    for key, value in d.items():
        if isinstance(value, Decimal):
            d[key] = float(value)
    return d

class MysqlConn(object):
    _db_pools = {}
    _master_min_cached = 0
    _master_max_cached = 1
    _master_max_connections = 1
    _master_block = False

    _lock = threading.Lock()

    @classmethod
    def config_pool(cls, master_config=None):
        MysqlConn._lock.acquire()
        try:
            if master_config is not None and MysqlConn._db_pools.has_key("master"):
                raise Exception("master db pool has been inited")

            if master_config is not None:
                cls._master_min_cached = master_config.get("min_cached", 0)
                cls._master_max_cached = master_config.get("max_cached", 0)
                cls._master_max_connections = master_config.get("max_connections", 5)
                cls._master_block = master_config.get("block", False)
        finally:
            MysqlConn._lock.release()

    @staticmethod
    def connection_statics():
        ret = {}
        max_ret = {}
        for db_type, db_pool in MysqlConn._db_pools.items():
            ret[db_type] = db_pool._connections
            max_ret[db_type] = db_pool._maxconnections
        return ret, max_ret


    def __init__(self, db_type="master"):
        if db_type not in ["master"]:
            raise Exception("db_type must be risk or master or reptile")
        if not MysqlConn._db_pools.has_key(db_type):
            MysqlConn._lock.acquire()
            try:
                if not MysqlConn._db_pools.has_key(db_type):
                    # database = "DLWSCluster-1a47446d-c59f-49fb-82a0-c63282469cc4"
                    # server = "apulis-sz-dev-infra01.sigsus.cn"
                    # username = "root"
                    # password = "apulis#2019#wednesday"
                    database = "DLWSCluster-572e5a5a-fba5-4380-afbd-9d6df31516a0"
                    server = "huawei-infra01.sigsus.cn"
                    username = "root"
                    password = "corona@2020@wuhan"
                    if db_type == "master":
                        MysqlConn._db_pools[db_type] = PooledDB(creator=MySQLdb, mincached=MysqlConn._master_min_cached,
                                                                maxcached=MysqlConn._master_max_cached,
                                                                maxconnections=MysqlConn._master_max_connections,
                                                                maxshared = 1,
                                                                host=server,
                                                                user=username,
                                                                passwd=password,
                                                                db=database,
                                                                use_unicode=False,
                                                                charset="utf8",
                                                                cursorclass=DictCursor,
                                                                blocking=MysqlConn._master_block,connect_timeout=1)

            finally:
                MysqlConn._lock.release()

        self._conn = MysqlConn._db_pools[db_type].connection(False)
        self._cur = self._conn.cursor()


    def select_one(self, sql, params=None):
        count = self._cur.execute(sql, params)
        if count > 0:
            return dict_decimal_to_float(self._cur.fetchone())
        else:
            return None

    def select_one_value(self, sql, params=None):
        count = self._cur.execute(sql, params)
        if count > 0:
            result = dict_decimal_to_float(self._cur.fetchone())
            return result.values()[0]
        else:
            return None

    def select_many(self, sql, params=None):
        count = self._cur.execute(sql, params)
        if count > 0:
            result = self._cur.fetchall()
            return map(lambda one: dict_decimal_to_float(one), result)
        else:
            return []

    def select_many_one_value(self, sql, params=None):
        count = self._cur.execute(sql, params)
        if count > 0:
            result = self._cur.fetchall()
            return map(lambda one: dict_decimal_to_float(one).values()[0], result)
        else:
            return []

    def insert_one(self, sql, params=None, return_auto_increament_id=False):
        self._cur.execute(sql, params)
        if return_auto_increament_id:
            return self._cur.lastrowid

    def insert_many(self, sql, params):
        count = self._cur.executemany(sql, params)
        return count

    def update(self, sql, param=None):
        return self._cur.execute(sql, param)

    def delete(self,sql,param=None):
        return self._cur.execute(sql,param)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._cur.close()
        self._conn.close()

    def executed(self):
        """获取刚刚执行的SQL语句
        _cur._executed 是私有属性，可能会在没有警告的情况下改变，所以本方法仅适用于调试时使用"""
        return self._cur._executed

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(exc_type)
            logging.error(exc_val)
            logging.error(traceback.format_exc())
        self.close()
        return False

@app.route('/')
def hello_world():
    with MysqlConn() as connect:
        a = connect.select_one("select * from account")
        print(a)
    return 'Hello World!'


if __name__ == '__main__':
    with MysqlConn() as connect:
        a = connect.select_one("select * from account")
    print a
