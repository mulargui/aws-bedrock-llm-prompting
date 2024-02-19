./infra/run.sh debug

# In case the container is running remote (ie in a cloud VM) the easiest solution
# is to create a ssh tunnel that routes all the traffic in a local port to the remote server
#    ssh -L 5678:localhost:5678 username@myremoteserver.com