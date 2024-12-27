import obspython as obs # type: ignore
import time

def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        print("Recording saved, refreshing buffer!")
        obs.obs_frontend_replay_buffer_stop()
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_STOPPED:
        time.sleep(1) # Arbitrary stop because OBS fails to reset buffer unless there's a 1000ms+ pause for some reason
        obs.obs_frontend_replay_buffer_start()
        print("Buffer has restarted")

def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)

def script_description():
    # TODO: Add more detail to this
    desc = (
        "<h1>Replay Buffer Restarter!</h1>"
        "<h2>Authored by The3D</h2>"
    )
    
    return desc