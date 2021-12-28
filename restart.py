import os, sys, time
 
# length of arguments
arg_length = len(sys.argv)

# paste original configuration file for dcplnx22840332
copy_orig_conf_332 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'"]

# paste original configuration file for dcplnx22865287
copy_orig_conf_287 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_orig http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_orig http-instance.conf'"]

# paste blue configuration file for dcplnx22840332
copy_blue_conf_332 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'"]

# paste blue configuration file for dcplnx22865287
copy_blue_conf_287 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_blue http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_blue http-instance.conf'"]

# paste green configuration file for dcplnx22840332
copy_green_conf_332 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'"]

# paste green configuration file for dcplnx22865287
copy_green_conf_287 = ["ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-batch-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern2-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-extern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern2-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-mshop-proxy/conf/; cp http-instance.conf_green http-instance.conf'", 
"ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/apps/apache-prod-tibet-intern-proxy/conf/; cp http-instance.conf_green http-instance.conf'"]

# graceful restart all proxy apaches for dcplnx22840332
restart_apaches_332 = "ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/scripts/; ./apaches_proxy.sh graceful'"

# graceful restart all proxy apaches for dcplnx22865287
restart_apaches_287 = "ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/scripts/; ./apaches_proxy.sh graceful'"

# delete text file with PIDs
delete_pids_file = "rm -rf pids.txt"

# find PID of all blue instances and store it to text file
store_blue_pids = ["ssh ecare@qde5nj ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qde5nj ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2d ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2d ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2f ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2f ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2b ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2b ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2h ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2h ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2k ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2k ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt"]

# find PID of all green instances and store it to text file
store_green_pids = ["ssh ecare@qde5nj ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qde5nj ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2d ps -ef | grep -i wildfly20_prod_11003 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2d ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2f ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2f ps -ef | grep -i wildfly20_prod_11004 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2b ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2b ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2h ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2h ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2k ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt",
"ssh ecare@qdef2k ps -ef | grep -i wildfly20_prod_11002 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt"]

# stop instances separately
stop_instances = ["ssh ecare@qde5nj kill -9 ",
"ssh ecare@qdef2d kill -9 ",
"ssh ecare@qdef2f kill -9 ",
"ssh ecare@qdef2b kill -9 ",
"ssh ecare@qdef2h kill -9 ",
"ssh ecare@qdef2k kill -9 "]

# start blue instances separately 
start_blue_instances = ["ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 '",
"ssh ecare@qdef2d 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2d 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2f 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2f 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2b 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2b 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2h 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2h 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2k 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2k 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'"]

# start green instances separately
start_green_instances = ["ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2d 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2d 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2f 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2f 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2b 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2b 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2h 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2h 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2k 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11001/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11001/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qdef2k 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11002/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11002/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'"]

# open text file, read PIDs stored in file, execute kill commands and close text file - stop instances proccess
def stop_instances_proc():
    file = open("pids.txt", "r")
    content = file.readlines() # read content of pids.txt file
    line_num = -1

    for cmnd in stop_instances:
        line_num += 1
        os.system(cmnd + content[line_num])
        line_num += 1
        os.system(cmnd + content[line_num])

    file.close()

# full restart method
def full():
    print("full")

# orig method
def orig():
    print("orig")

# blue method
def blue():
    blueNR()

    os.system(delete_pids_file)
    for cmnd in store_blue_pids:
        os.system(cmnd)

    stop_instances_proc()
    time.sleep(5) # delay script for 5 seconds

    for cmnd in start_blue_instances:
        os.system(cmnd)

# green method
def green():
    greenNR()

    os.system(delete_pids_file)
    for cmnd in store_green_pids:
        os.system(cmnd)

    stop_instances_proc()
    time.sleep(5) # delay script for 5 seconds

    for cmnd in start_green_instances:
        os.system(cmnd)

# orig no restart method
def origNR():
    for cmnd in copy_orig_conf_332:
        os.system(cmnd) 
    os.system(restart_apaches_332)
    for cmnd in copy_orig_conf_287:
        os.system(cmnd) 
    os.system(restart_apaches_287)

# blue no restart method
def blueNR():
    for cmnd in copy_blue_conf_332:
        os.system(cmnd) 
    os.system(restart_apaches_332)
    for cmnd in copy_blue_conf_287:
        os.system(cmnd) 
    os.system(restart_apaches_287)

# green no restart method
def greenNR():
    for cmnd in copy_green_conf_332:
        os.system(cmnd) 
    os.system(restart_apaches_332)
    for cmnd in copy_green_conf_287:
        os.system(cmnd) 
    os.system(restart_apaches_287)

# full restart
if arg_length == 1:
    full()

# orig, blue and green
elif arg_length == 2 :

    if sys.argv[1] == "orig":
        orig()

    elif sys.argv[1] == "blue":
        blue()

    elif sys.argv[1] == "green":
        green()

    else:
        print("Wrong argument")

# orig, blue and green with no restart
elif arg_length == 3:

    if sys.argv[1] == "orig":
        if sys.argv[2] == "norestart":
            origNR()
        else:
            print("Wrong argument")

    elif sys.argv[1] == "blue":
        if sys.argv[2] == "norestart":
            blueNR()
        else:
            print("Wrong argument")

    elif sys.argv[1] == "green":
        if sys.argv[2] == "norestart":
            greenNR()
        else:
            print("Wrong argument")

    else:
        print("Wrong argument")

else:
    print("Too many arguments")
