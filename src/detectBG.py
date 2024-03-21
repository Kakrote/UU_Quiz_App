import psutil

def is_process_running(process_name):
  """
  Checks if a process with the given name is running.

  Args:
      process_name: The name of the process (e.g., "chrome.exe").

  Returns:
      True if the process is found, False otherwise.
  """
  for process in psutil.process_iter(['name']):
    if process.info['name'] == process_name:
      return True
  return False

# Example usage
if is_process_running("chrome.exe"):
  print("Chrome is running")
else:
  print("Chrome is not running")

  
if is_process_running("msedge.exe"):
  print("msedge is running")
else:
  print("msedge is not running")
