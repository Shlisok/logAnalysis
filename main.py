import pandas as pd
LOG_TAG = '<PNB4001>'


# 读取日志文件并分析
def read_log_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        lines = [line.strip() for line in file if line.strip()]
    # 两种日志
    DNS_list = []
    HTTP_list = []
    for line in lines:
        result = log_sort(line)
        if result[0]:
            # 根据日志字段数量判断日志类型
            if result[1] == 10:
                DNS_list.append(line)
            elif result[1] == 13:
                HTTP_list.append(line)

    return DNS_list, HTTP_list


# 判断是否是正确日志
def log_sort(log_str):
    return LOG_TAG in log_str, len(log_str.split())

def list_to_df(DNS_list, HTTP_list):
    DNS_data = pd.DataFrame([x.split() for x in DNS_list],
                            columns=['时间戳', '记录网关', '标识符', '日志批次', '上网设备MAC地址',
                                     '上网设备IP地址', '源端口', 'DNS服务器地址', '目的端口', '查询地址'])
    HTTP_data = pd.DataFrame([x.split() for x in HTTP_list],
                             columns=['时间戳', '记录网关', '标识符', '日志批次', '上网设备MAC地址',
                                      '上网设备IP地址', '源端口', '目的地址', '目的端口', '未知符号',
                                      '方式', '目的域名', 'url详情'])
    return DNS_data, HTTP_data




if __name__ == '__main__':
    dns_list, http_list = read_log_file('files/192.168.35.2.log')
    dns_df, http_df = list_to_df(dns_list, http_list)


