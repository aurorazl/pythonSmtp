from test_case import *
import time

class SymbolMemberShip:
    def __init__(self, symbol, exchange, group):
        self.symbol = symbol
        self.exchange = exchange
        self.group = group

# 实现一个虚拟时间的TTL字典
class TTLCache:

    def __init__(self,ttl):
        self.ttl = ttl
        self.__DATA = {}
    def __getitem__(self, item):
        return self.__DATA[item]
    def __setitem__(self, key, value):
        self.__DATA[key]=value
    def items(self,time):
        tmp=[]
        for k,v in self.__DATA.items():
            if k == "alert":
                if v < time-self.ttl:
                    tmp.append(k)
            else:
                if k > time-self.ttl:
                    yield k,v
                else:
                    tmp.append(k)
        for one in tmp:
            self.__DATA.pop(one)
    def __contains__(self, item):
        return True if item in self.__DATA else False

# 可以在此基础上进行任意的设计和修改
class TradeMonitor:
    def __init__(self):
        pass

    def find_symbol_or_group_or_exchange(self,name,type):
        for one in Global_Data[type]:
            if one.name == name:
                return one
        return None

    def on_trade(self, trade):
        # 找出所属的SYMBOL、GROUP、EXCHANGE
        THIS_SYMBOL = self.find_symbol_or_group_or_exchange(trade["name"],"symbols")
        THIS_GROUP = self.find_symbol_or_group_or_exchange(THIS_SYMBOL.group_name,"groups")
        THIS_EXCHANGE = self.find_symbol_or_group_or_exchange(THIS_SYMBOL.exchange_name,"exchanges")
        Global_Data[THIS_SYMBOL.name] = SymbolMemberShip(THIS_SYMBOL,THIS_EXCHANGE,THIS_GROUP)

        # 根据interval来生成缓存cache，quantity和delta分开
        Global_Data.setdefault("quantity", {})
        Global_Data.setdefault("delta", {})
        Global_Data["quantity"].setdefault(trade["name"],TTLCache(ttl=THIS_SYMBOL.quantity_interval))
        Global_Data["delta"].setdefault(trade["name"],TTLCache(ttl=THIS_SYMBOL.quantity_interval))

        # 缓存当前交易
        Global_Data["quantity"][trade["name"]][trade["time"]] = trade
        Global_Data["delta"][trade["name"]][trade["time"]] = trade

        # 计算累计结果
        total_quantity = [0,0,0]
        total_delta = [0,0,0]
        same_group_symbols = [i.name for i in Global_Data["symbols"] if i.group_name == THIS_GROUP.name]
        same_exchange_symbols = [i.name for i in Global_Data["symbols"] if i.exchange_name == THIS_EXCHANGE.name]
        for symbol,symbol_ttl in Global_Data["quantity"].items():
            if symbol == THIS_SYMBOL.name:
                for trace_time,trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time!="alert":
                        total_quantity[0]+=1
            if symbol in same_exchange_symbols:
                for trace_time,trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time != "alert":
                        total_quantity[1]+=1
            if symbol in same_group_symbols:
                for trace_time,trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time != "alert":
                        total_quantity[2]+=1


        for symbol,symbol_ttl in Global_Data["delta"].items():

            if symbol == THIS_SYMBOL.name:

                for trace_time,trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time != "alert":
                        total_delta[0] += trace_info["quantity"] * trace_info["price"] * (1 if trace_info["side"] == "BUY" else -1)
            if symbol in same_exchange_symbols:

                for trace_time, trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time != "alert":
                        total_delta[1] += trace_info["quantity"] * trace_info["price"] * (
                            1 if trace_info["side"] == "BUY" else -1)
            if symbol in same_group_symbols:
                for trace_time, trace_info in symbol_ttl.items(trade["time"]):
                    if trace_time != "alert":
                        total_delta[2] += trace_info["quantity"] * trace_info["price"] * (
                            1 if trace_info["side"] == "BUY" else -1)

        for index in range(len(total_quantity)):
            if total_quantity[index]<0:
                total_quantity[index] *= -1
        for index in range(len(total_delta)):
            if total_delta[index]<0:
                total_delta[index] *= -1

        # 按照当前symbol、exchange、group的顺序报警
        alert_list = [(THIS_SYMBOL,[THIS_SYMBOL.name],"symbol"),(THIS_EXCHANGE,same_exchange_symbols,"exchange"),(THIS_GROUP,same_group_symbols,"group")]
        for index,(alert_item,symbol_list,asource) in enumerate(alert_list,0):

            if alert_item.quantity_limit < total_quantity[index]:
                for one_symbol in symbol_list:
                    self.traggle_alert(one_symbol, "quantity",alert_item.quantity_limit,total_quantity[index],alert_item.name,trade["time"])

            if alert_item.delta_limit < total_delta[index]:
                for one_symbol in symbol_list:
                    self.traggle_alert(one_symbol, "delta",alert_item.delta_limit,total_delta[index],alert_item.name,trade["time"])
        print(trade,total_quantity,total_delta)

    @staticmethod
    def traggle_alert(symbol_name,atype,threshold,current_value,asource,alert_time):
        if "alert" not in Global_Data[atype][symbol_name]:
            Global_Data[atype][symbol_name]["alert"] = alert_time
            msg = " threshold: {}  current: {} reason: {} exceed limit".format(threshold,current_value,asource)
            TradeMonitor.alarm(alert_time, symbol_name, atype=atype,msg=msg)

    @staticmethod
    def alarm(atime, name, atype='quantity',msg=""):
        alarm_msg = '累计成交量报警'+msg
        if atype == 'delta':
            alarm_msg = '累计Delta报警'+msg
        print(atime, name, alarm_msg)


if __name__ == "__main__":
    monitor = TradeMonitor()

    load_param_data1()
    load_trade_data1(monitor)

    load_param_data2()
    load_trade_data2(monitor)
