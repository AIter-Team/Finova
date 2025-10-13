from datetime import datetime

def get_current_time() -> dict:
    """Get current time
    
    Returns:
        dict: A dictionary containing current timestamp.
    """
    return({"Current Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})