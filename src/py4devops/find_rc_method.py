import os

def find_rc(rc_name=".examplerc"):
    """
    Your tool might look first for an environment variable that defines which .rc file to use, 
and in its absence, check the working directory, and then the user’s home directory 
and lastly the curr dir of this file.
    """
    
    # Check for Env variable
    var_name = "EXAMPLERC_DIR"
    # Check whether the environment variable exists in the current environment.
    if var_name in os.environ:
        # Use join to construct a path with the environment variable name. This will look something like $EXAMPLERC_DIR/.examplerc.
        var_path = os.path.join(f"${var_name}", rc_name)
        # Expand the environment variable to insert its value into the path.
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        # Check to see if the file exists.
        if os.path.exists(config_path):
            return config_path

    # Check the current working directory
    # Construct a path using the current working directory.
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check user home directory
    # Use the expanduser function to get the path to the user’s home directory.
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check Directory of This File
    # Expand the relative path stored in file to an absolute path.
    file_path = os.path.abspath(__file__)
    # Use dirname to get the path to the directory holding the current file.
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")

find_rc(".examplerc")