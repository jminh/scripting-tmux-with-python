import libtmux

server = libtmux.Server()

############################
# session: pelican-env
############################

s = server.new_session('pelican-env', kill_session=True)

  ############################
  # window: p
  ############################

w = s.attached_window
w.rename_window('p')

    ############################
    # pane
    ############################

p = w.attached_pane
p.send_keys('ls')
p.send_keys('cd /Users/ming/back_hoy/backup_arch/new/ming_pelican_blog')
p.send_keys('source activate test_development_env')
