#!/usr/bin/env bash

############################
# session: run-mongodb
############################

SESSION=run-mongodb

tmux -2 new-session -d -s ${SESSION}

  ############################
  # window: run-mongo
  ############################

tmux rename-window -t ${SESSION}:0 'run-mongo'

    ############################
    # pane
    ############################

tmux send-keys "cd ~" C-m
#p.send_keys('mongod --config mongod_config.txt --rest')


  ############################
  # window: run-restheart
  ############################

tmux new-window -t ${SESSION}:1 -n 'run-restheart'

    ############################
    # pane
    ############################

tmux send-keys "cd /tmp" C-m
#restheart_p.send_keys('java -server -jar restheart.jar')

  ############################
  # window: run-vulture
  ############################

tmux new-window -t ${SESSION}:2 -n 'run-vulture'

    ############################
    # pane
    ############################

tmux send-keys "cd /home" C-m
#vulture_p.send_keys('cd ~/restheart-2.0.0')

###########################
# set default window
###########################

tmux select-window -t $SESSION:0
