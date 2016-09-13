
import libtmux

server = libtmux.Server()

############################
# session: run-mongodb
############################

#session = server.new_session('run-mongodb', kill_session=True)
session = server.new_session('run-mongodb')

  ############################
  # window: run-mongo
  ############################

w = session.attached_window
w.rename_window('run-mongo')

    ############################
    # pane
    ############################

p = w.attached_pane

p.send_keys('cd ~')
p.send_keys('mongod --config mongod_config.txt --rest')


  ############################
  # window: run-restheart
  ############################

restheart_w = session.new_window('run-resthear')

    ############################
    # pane
    ############################

restheart_p = restheart_w.attached_pane
restheart_p.send_keys('cd ~/restheart-2.0.0')
#restheart_p.send_keys('java -server -jar restheart.jar')

  ############################
  # window: run-vulture
  ############################

vulture_w = session.new_window('run-vulture')

    ############################
    # pane
    ############################

vulture_p = vulture_w.attached_pane
vulture_p.send_keys('cd ~/restheart-2.0.0')
#vulture_p.send_keys('cd ~/restheart-2.0.0')







