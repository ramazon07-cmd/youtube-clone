from django import forms

class VideoUploadForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Enter video title'
            }
            ),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'placeholder': 'Enter video description'
            }
            ),
        required=False
    )
    video_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Choose video file',
                'accept': 'video/*'
            }
            ),
    )

    def clean_video_file(self):
        video_file = self.cleaned_data.get('video_file')
        if video_file:
            if video_file.size > 100 * 1024 * 1024:  # Limit to 100MB
                raise forms.ValidationError("Video file size must be under 100MB.")
            allowed_types = ['video/mp4', 'video/avi', 'video/mov', 'video/wmv']
            if video_file.content_type not in allowed_types:
                raise forms.ValidationError("Unsupported video format. Allowed formats: MP4, AVI, MOV, WMV.")
            return video_file
        else:
            raise forms.ValidationError("Please upload a video file.")
        






























