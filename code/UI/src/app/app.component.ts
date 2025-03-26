import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'UI';
  selectedFile: File | null = null;
  inputData: string = '';
  // constructor(private apiService: ApiService) {}

  onSubmit(): void {
    alert('Form submitted!');
    console.log('Form submitted!');
    if (!this.selectedFile || !this.inputData) {
      alert('Please select a file and enter input data.');
      return;
    }

    // const formData = new FormData();
    // formData.append('file', this.selectedFile);
    // formData.append('inputData', this.inputData);

    // this.apiService.uploadEmlFile(formData).subscribe(
    //   (response) => {
    //     console.log('Response from API:', response);
    //     alert('File and data uploaded successfully!');
    //   },
    //   (error) => {
    //     console.error('Error uploading file:', error);
    //     alert('Failed to upload file.');
    //   }
    // );
  }

  // // Handle file selection
  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

}
