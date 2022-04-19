import os, time

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
"ssh ecare@qde5nj kill -9 ",
"ssh ecare@qdef2d kill -9 ",
"ssh ecare@qdef2d kill -9 ",
"ssh ecare@qdef2f kill -9 ",
"ssh ecare@qdef2f kill -9 ",
"ssh ecare@qdef2b kill -9 ",
"ssh ecare@qdef2b kill -9 ",
"ssh ecare@qdef2h kill -9 ",
"ssh ecare@qdef2h kill -9 ",
"ssh ecare@qdef2k kill -9 ",
"ssh ecare@qdef2k kill -9 "]

# start blue instances separately 
start_blue_instances = ["ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11003/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11003/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
"ssh ecare@qde5nj 'export RUN_CONF=/home/ecare/apps/wildfly20_prod_11004/configuration/standalone.conf && cd /home/ecare/apps/wildfly/wildfly-20.0.1.Final/bin/ && nohup ./standalone.sh -Djboss.server.base.dir=/home/ecare/apps/wildfly20_prod_11004/ -b=0.0.0.0 -bmanagement=0.0.0.0 >/dev/null 2>&1 &'",
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

# check if blue instances are really started (deployed)
check_blue_deployed = ["ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt"]

# check if green instances are really started (deployed)
check_green_deployed = ["ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c deployed >> state_deployed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c deployed >> state_deployed.txt"]

# check if blue instances are failed
check_blue_failed = ["ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt"]

# check if green instances are failed
check_green_failed = ["ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qde5nj ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11003/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2d ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2f ls -la /home/ecare/apps/wildfly20_prod_11004/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2b ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2h ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11001/deployments | grep -c failed >> state_failed.txt",
"ssh ecare@qdef2k ls -la /home/ecare/apps/wildfly20_prod_11002/deployments | grep -c failed >> state_failed.txt"]

# delete text file with PIDs
delete_pids_file = "rm pids.txt"

# delete text file with deployed instances
delete_deployed_file = "rm state_deployed.txt"

# delete text file with failed instances
delete_failed_file = "rm state_failed.txt"

# name of blue instances
blue_instances = ["QDE5NJ(tko4s2a1r0) - instance 11003 ",
"QDE5NJ(tko4s2a1r0) - instance 11004 ",
"QDEF2D(tko4s2a390) - instance 11001 ",
"QDEF2D(tko4s2a390) - instance 11002 ",
"QDEF2F(tko4s2a3a0) - instance 11002 ",
"QDEF2F(tko4s2a3a0) - instance 11003 ",
"QDEF2B(tko4s2a3b0) - instance 11003 ",
"QDEF2B(tko4s2a3b0) - instance 11004 ",
"QDEF2H(tko4s2a6b0) - instance 11003 ",
"QDEF2H(tko4s2a6b0) - instance 11004 ",
"QDEF2K(tko4s2a6c0) - instance 11003 ",
"QDEF2K(tko4s2a6c0) - instance 11004 "]

# name of green instances
green_instances = ["QDE5NJ(tko4s2a1r0) - instance 11001 ",
"QDE5NJ(tko4s2a1r0) - instance 11002 ",
"QDEF2D(tko4s2a390) - instance 11003 ",
"QDEF2D(tko4s2a390) - instance 11004 ",
"QDEF2F(tko4s2a3a0) - instance 11001 ",
"QDEF2F(tko4s2a3a0) - instance 11004 ",
"QDEF2B(tko4s2a3b0) - instance 11001 ",
"QDEF2B(tko4s2a3b0) - instance 11002 ",
"QDEF2H(tko4s2a6b0) - instance 11001 ",
"QDEF2H(tko4s2a6b0) - instance 11002 ",
"QDEF2K(tko4s2a6c0) - instance 11001 ",
"QDEF2K(tko4s2a6c0) - instance 11002 "]

# state of deployed instance 
deployed_message = ["deploying", "deployed"]

# store pids from instances to txt file
def store_pids_to_file(instance_color):
    os.system(delete_pids_file)
    if (instance_color == "blue"):
        for cmnd in store_blue_pids:
            os.system(cmnd)
    else: 
        for cmnd in store_green_pids:
            os.system(cmnd)

# stop one instance process
def stop_one_instance(line_number):
    file = open("pids.txt", "r")
    PID = file.readlines() # read content of pids.txt file

    os.system(stop_instances[line_number]  + PID[line_number])

    file.close()

# restart only one instance from the input without checking
def restart_instance_without_check(instance_color, line_number):
    # stop instance
    store_pids_to_file(instance_color)
    stop_one_instance(line_number)
    if (instance_color == "blue"):
        print("\n %s is successfully stopped. Restarting instance." %(blue_instances[line_number]))
    else:
        print("\n %s is successfully stopped. Restarting instance." %(green_instances[line_number]))

    time.sleep(5) # delay script for 5 seconds

    # start instance
    if (instance_color == "blue"):
        os.system(start_blue_instances[line_number])
        print("%s is starting again. \n" %(blue_instances[line_number]))
    else: 
        os.system(start_green_instances[line_number])
        print("%s is starting again. \n" %(green_instances[line_number]))

# restart only one instance from the input and check instance
def restart_instance(instance_color, line_number):
    restart_instance_without_check(instance_color, line_number)

    time.sleep(120) # delay script for 2 minutes

    # check instance if is successfully restarted and set timer
    timer = 0
    check_state = check_instance_after_restart(instance_color, line_number, timer) 

    # if state is "check", then check instance state again, increase timer with 1 second
    while (check_state == "check"):
        time.sleep(10) # wait 10 seconds before next check
        timer += 1
        check_state = check_instance_after_restart(instance_color, line_number, timer)
    
    # restart instance again
    if check_state == "restart":
        restart_instance(instance_color, line_number)

    # successfully deployed instance
    if check_state == "deployed":
        if (instance_color == "blue"):
            print("\n %s is successfully deployed." %(blue_instances[line_number]))  
        else:
            print("\n %s is successfully deployed." %(green_instances[line_number]))      

# check deploying of restarted instance
def check_instance_after_restart(instance_color, line_number, timer): 
    # delete old state files   
    os.system(delete_failed_file)
    os.system(delete_deployed_file)

    # check instance color, then check instance state and write it to .txt file
    if (instance_color == "blue"):
        os.system(check_blue_failed[line_number])
        os.system(check_blue_deployed[line_number])	
    else: 
        os.system(check_green_failed[line_number])
        os.system(check_green_deployed[line_number])	

    # read line from state files
    file = open("state_failed.txt", "r")
    contentFailed = file.readline() # read content of failed.txt file
    file.close()

    file = open("state_deployed.txt", "r")
    contentDeployed = file.readline() # read content of deployed.txt file
    file.close()
    
    # check if instance is .failed,  if yes, restart this instance
    if contentFailed == 1:
        if (instance_color == "blue"):
            print("\n %s is .failed." %(blue_instances[line_number]))
        else: 
            print("\n %s is .failed." %(green_instances[line_number]))
        return "restart"

    # check if instance is .deployed
    if contentDeployed == 1:		
        return "deployed"
    
    # if instance is stuck after 8 minutes, restart this instance
    if timer == 48:		
        return "restart"

    return "check"

# full restart
def full():
    blue_green_restart("blue")
    blue_green_restart("green")
    orig()
    print("Full application restart is successfully ended. \n")

# orig configuration files
def orig():
    for cmnd in copy_orig_conf_332:
        os.system(cmnd) 
    os.system(restart_apaches_332)

    for cmnd in copy_orig_conf_287:
        os.system(cmnd) 
    os.system(restart_apaches_287)

    print("Original configuration files are on. Apaches were restarted.")

# blue green restart 
def blue_green_restart(instance_color):
    blue_green_no_restart(instance_color)

    store_pids_to_file(instance_color)

    print("Stopping all %s instances." %instance_color)
    for line_number in range(0, 11):
        stop_one_instance(line_number)

    time.sleep(5) # delay script for 5 seconds

    print("Starting all %s instances." %instance_color)
    if (instance_color == "blue"):
        for cmnd in start_blue_instances: 
            os.system(cmnd)
    else: 
        for cmnd in start_green_instances: 
            os.system(cmnd)

    time.sleep(120) # delay script for 2 minutes
    counter_deployed = 0
    timer = 0 
    while counter_deployed != 12 or timer != 48:
        time.sleep(10) # delay script for 10 seconds
        counter_deployed = 0
        timer += 1
        
        os.system(delete_deployed_file)
        os.system(delete_failed_file)

        if (instance_color == "blue"):
            for cmnd in check_blue_deployed:
                os.system(cmnd)
                    
            for cmnd in check_blue_failed:
                os.system(cmnd)		
        else: 
            for cmnd in check_green_deployed:
                os.system(cmnd)
                    
            for cmnd in check_green_failed:
                os.system(cmnd)	

        file = open("state_deployed.txt", "r")
        contentDeployed = file.readlines() # read content of deployed.txt file
        file.close()
        
        file = open("state_failed.txt", "r")
        contentFailed = file.readlines() # read content of failed.txt file
        file.close()
        
        # check how many instances are failed, restart these instances
        line_failed_counter = -1
        for failed in contentFailed:
            line_failed_counter += 1
            if failed == 1:
                if (instance_color == "blue"):
                    print("\n %s is failed." %(blue_instances[line_failed_counter]))
                else:
                    print("\n %s is failed." %(green_instances[line_failed_counter]))
                timer = 0
                restart_instance_without_check(instance_color, line_failed_counter)

        # check how many instances are deployed
        line_deployed_counter = -1
        for deployed in contentDeployed:
            line_deployed_counter += 1
            if (instance_color == "blue"):
                print("%s is %s." %(blue_instances[line_deployed_counter], deployed_message[deployed]))
            else:
                print("%s is %s." %(green_instances[line_deployed_counter], deployed_message[deployed]))
            if deployed == 1:			
                counter_deployed =+ 1
            else:
                # if instances are stuck after 8 minutes, restart these instances
                if timer == 47:
                    if (instance_color == "blue"):
                        print("\n %s is stuck. Restarting instance." %(blue_instances[line_deployed_counter]))
                    else:
                        print("\n %s is stuck. Restarting instance." %(green_instances[line_deployed_counter]))
                    timer = 0
                    restart_instance_without_check(instance_color, line_deployed_counter) 	

    print("All %s instances are restarted successfully. \n" %instance_color)

# blue green no restart 
def blue_green_no_restart(instance_color):

    if (instance_color == "blue"):
        for cmnd in copy_blue_conf_332:
            os.system(cmnd) 
        os.system(restart_apaches_332)

        for cmnd in copy_blue_conf_287:
            os.system(cmnd) 
        os.system(restart_apaches_287)

        print("Blue configuration files are on. Apaches were restarted.")
    else:
        for cmnd in copy_green_conf_332:
            os.system(cmnd) 
        os.system(restart_apaches_332)

        for cmnd in copy_green_conf_287:
            os.system(cmnd) 
        os.system(restart_apaches_287)

        print("Green configuration files are on. Apaches were restarted.")

# Main method
def main():
    print(" Hello! Please, choose one of options: ")
    print("1 - Full app restart")
    print("2 - Original apache profile + app restart")
    print("3 - Blue apache profile + app restart")
    print("4 - Green apache profile + app restart")
    print("5 - Blue apache profile without app restart")
    print("6 - Green apache profile without app restart")
    print("7 - Restart only one instance")
    restart_option = input("Your option: ")

    if (restart_option == "1"):
        full()
    elif (restart_option == "2"):
        orig()
    elif (restart_option == "3"):
        blue_green_restart("blue")
    elif (restart_option == "4"):
        blue_green_restart("green")
    elif (restart_option == "5"):
        blue_green_no_restart("blue")
    elif (restart_option == "6"):
        blue_green_no_restart("green")
    elif (restart_option == "7"):
        print("\n Please, choose one of options: ")
        print("1 - Blue instances")
        print("2 - Green instances")
        color_option = input("Your option: ")

        if (color_option == "1"):
            print("\n Please, choose one of options: ")
            print("0 - QDE5NJ(tko4s2a1r0) - instance 11003")
            print("1 - QDE5NJ(tko4s2a1r0) - instance 11004")
            print("2 - QDEF2D(tko4s2a390) - instance 11001")
            print("3 - QDEF2D(tko4s2a390) - instance 11002")
            print("4 - QDEF2F(tko4s2a3a0) - instance 11002")
            print("5 - QDEF2F(tko4s2a3a0) - instance 11003")
            print("6 - QDEF2B(tko4s2a3b0) - instance 11003")
            print("7 - QDEF2B(tko4s2a3b0) - instance 11004")
            print("8 - QDEF2H(tko4s2a6b0) - instance 11003")
            print("9 - QDEF2H(tko4s2a6b0) - instance 11004")
            print("10 - QDEF2K(tko4s2a6c0) - instance 11003")
            print("11 - QDEF2K(tko4s2a6c0) - instance 11004")
            instance_option = input("Your option: ")

            if (instance_option == "0" or instance_option == "1" or instance_option == "2" or instance_option == "3"
            or instance_option == "4" or instance_option == "5" or instance_option == "6" or instance_option == "7" 
            or instance_option == "8" or instance_option == "9" or instance_option == "10" or instance_option == "11"):
                restart_instance("blue", instance_option)
            else: 
                print("Wrong input, please try again. \n")
                main()
            
        elif (color_option == "2"):
            print("\n Please, choose one of options: ")
            print("0 - QDE5NJ(tko4s2a1r0) - instance 11001")
            print("1 - QDE5NJ(tko4s2a1r0) - instance 11002")
            print("2 - QDEF2D(tko4s2a390) - instance 11003")
            print("3 - QDEF2D(tko4s2a390) - instance 11004")
            print("4 - QDEF2F(tko4s2a3a0) - instance 11001")
            print("5 - QDEF2F(tko4s2a3a0) - instance 11004")
            print("6 - QDEF2B(tko4s2a3b0) - instance 11001")
            print("7 - QDEF2B(tko4s2a3b0) - instance 11002")
            print("8 - QDEF2H(tko4s2a6b0) - instance 11001")
            print("9 - QDEF2H(tko4s2a6b0) - instance 11002")
            print("10 - QDEF2K(tko4s2a6c0) - instance 11001")
            print("11 - QDEF2K(tko4s2a6c0) - instance 11002")
            instance_option = input("Your option: ")
            
            if (instance_option == "0" or instance_option == "1" or instance_option == "2" or instance_option == "3"
            or instance_option == "4" or instance_option == "5" or instance_option == "6" or instance_option == "7" 
            or instance_option == "8" or instance_option == "9" or instance_option == "10" or instance_option == "11"):
                restart_instance("green", instance_option)
            else: 
                print("Wrong input, please try again. \n")
                main()
        else:
            print("Wrong input, please try again. \n")
            main()
    else:
        print("Wrong input, please try again. \n")
        main()

# Start of the script
main()