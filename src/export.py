import os

class Export:
    def __init__(self):
        self.events = []
        self.errorMessage = ""
        self.exportPath = ""
    
    def loadEvents(self, events):
        if not isinstance(events, list):
            raise ValueError("Events must be a list")
        self.events = events
        return True
    
    def exportEvents(self, filepath):
        if not self.events:
            self.errorMessage = "No events available for export."
            return False
        
        if not filepath:
            self.errorMessage = "Export path cannot be empty"
            return False
        
        try:
            with open(filepath, "w") as f:
                f.write("SYLLABUS EVENTS\n")
                f.write("=" * 50 + "\n\n")
                
                for event in self.events:
                    date = event.get("date", "")
                    title = event.get("title", "")
                    f.write("Date: " + date + "\n")
                    f.write("Title: " + title + "\n")
                    f.write("-" * 50 + "\n")
            
            self.exportPath = filepath
            return True
            
        except IOError as e:
            self.errorMessage = "Export failed. " + str(e)
            return False
        except Exception as e:
            self.errorMessage = "Export failed. " + str(e)
            return False
    
    def getEventCount(self):
        return len(self.events)
