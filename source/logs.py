class Loggers(object):
    
    def __init__(self , filename) -> None:
        self.filename = filename
    
    def _write_logs(self , type , msg):
        
        with open(self.filename, 'a') as file:
            file.write(f"[{type}] message was = > {msg}\n")
            
    def info(self , msg):
        self._write_logs(type="info" , msg=msg)
        
    def error(self , msg):
        self._write_logs(type="error" , msg=msg)
    
    def warning(self , msg):
        self._write_logs(type="warning" , msg=msg)
        
        
