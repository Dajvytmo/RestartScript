import os, sys
 
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
restart_apaches_332 = os.system("ssh 2a00:0da9:0004:202e:60fd:0000:2284:0332 'cd /home/ecare/scripts/; ./apaches_proxy.sh graceful'")

# graceful restart all proxy apaches for dcplnx22865287
restart_apaches_287 = os.system("ssh 2a00:0da9:0004:202e:60fd:0000:2286:5287 'cd /home/ecare/scripts/; ./apaches_proxy.sh graceful'")

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

# full restart method
def full():
    print("full")

# orig method
def orig():
    os.system("rm -rf pids.txt")
    os.system("ssh ecare@qde5nj ps -ef | grep -i wildfly20_prod_11001 | grep -v grep | grep keystore | gawk '{print $2}' >> pids.txt")

# blue method
def blue():
    for cmnd in start_blue_instances:
        os.system(cmnd)

# green method
def green():
    for cmnd in start_green_instances:
        os.system(cmnd)

# orig no restart method
def origNR():
    for cmnd in copy_orig_conf_332:
        os.system(cmnd) 
    restart_apaches_332
    for cmnd in copy_orig_conf_287:
        os.system(cmnd) 
    restart_apaches_287

# blue no restart method
def blueNR():
    for cmnd in copy_blue_conf_332:
        os.system(cmnd) 
    restart_apaches_332
    for cmnd in copy_blue_conf_287:
        os.system(cmnd) 
    restart_apaches_287

# green no restart method
def greenNR():
    for cmnd in copy_green_conf_332:
        os.system(cmnd) 
    restart_apaches_332
    for cmnd in copy_green_conf_287:
        os.system(cmnd) 
    restart_apaches_287

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
