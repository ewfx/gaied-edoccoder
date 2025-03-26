import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { NgModule } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/compiler';
import { ApiService } from './services/api.service';

@NgModule({
  declarations: [AppComponent],
  imports: [
    HttpClientModule, // Add this
    FormsModule, // Add this for two-way data binding
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  providers: [ApiService],
  exports: [AppComponent],
  bootstrap: [AppComponent],
})
export class AppModule {}

