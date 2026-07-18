import subprocess

class AudioDevice:
    @staticmethod
    def list_outputs():
        try:
            result = subprocess.run(
                ["wpctl", "status"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    print(AudioDevice.list_outputs())
