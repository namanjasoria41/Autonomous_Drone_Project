# Main Mission Controller
from modules.takeoff import autonomous_takeoff
from modules.kml_parser import load_kml_mission
from modules.video_stream import start_video_stream
from modules.object_detection import detect_survivors
from modules.speaker import activate_speaker
from modules.payload import drop_payload
from modules.failsafe import check_failsafe_conditions
from modules.state_machine import run_mission_state_machine

def main():
    print("[Mission] Starting mission...")
    autonomous_takeoff()
    waypoints = load_kml_mission("mission.kml")
    start_video_stream()
    run_mission_state_machine(waypoints)

if __name__ == "__main__":
    main()
