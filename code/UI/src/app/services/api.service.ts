import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://127.0.0.1:5000'; // Replace with your Python API base URL

  constructor(private http: HttpClient) {}

  // Upload .eml file and input data
  uploadEmlFile(formData: FormData): Observable<any> {
    return this.http.post(`${this.baseUrl}/upload-eml`, formData);
  }
}
