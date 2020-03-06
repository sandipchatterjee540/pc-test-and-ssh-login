import psutil

def disc_use():
    disk_part=psutil.disk_partitions()
    dic={}
    for i in range(0,len(disk_part)):
        try:    
            drv=str(disk_part[i].mountpoint[:2])
            #print (disk_part[i].mountpoint[:1] + str(" DRIVE : ") + str( psutil.disk_usage(str(drv)).percent) +str("% Usage"))
            dic[disk_part[i].mountpoint[0:1]]=str( psutil.disk_usage(str(drv)).percent)
        except PermissionError:
            continue
    return dic

def cpu_use():
    # core=psutil.cpu_count(logical=False)
    # total_core=psutil.cpu_count()
    # cpu_persent=psutil.cpu_percent(interval=None)
    ip=psutil.net_if_addrs()
    # print (type(ip))
    print(ip)

def mem_use():
    #dic={}
    mem=psutil.virtual_memory()
    #dic["MEMORY"]=str(mem.percent)
    return mem.percent

#disc_use()
#me_use()
#cpu_use()
