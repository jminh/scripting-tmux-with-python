import libtmux

server = libtmux.Server()

############################
# session: run-jenkins
############################

#session = server.new_session('run-jenkins', kill_session=True)
session = libtmux.new_session('run-jenkins')

  ############################
  # window: run-jenkins
  ############################

w = session.attached_window
w.rename_window('run-jenkins')

    ############################
    # pane
    ############################

p = w.attached_pane

p.send_keys('setenv JAVA_HOME ~/jdk1.8.0_73')
p.send_keys('setenv PATH $JAVA_HOME/bin:$PATH')
p.send_keys('java -version')
#p.send_keys('java -jar jenkins.war')
