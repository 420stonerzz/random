# capability_analyzer.py
class CapabilityAnalyzer:
    def analyze(self, user_request):
        request_lower = user_request.lower()
        if any(word in request_lower for word in ['disney', 'netflix', 'hulu', 'stream']):
            return "media_playback"
        elif any(word in request_lower for word in ['bubble', 'website', 'web app']):
            return "bubble_automation" 
        else:
            return "web_automation"