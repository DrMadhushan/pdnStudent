import { AuthService } from './../shared/services/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss']
})
export class ResetPasswordComponent implements OnInit {

  constructor(public authService: AuthService) { }
  mailSent:boolean = false;
  ngOnInit(): void {
  }

  onClick(email:any){
    if(email != null){
      this.authService.sendResetPasswordEmail(email);
      this.authService.logout();
      this.mailSent = true;
    }
  }
}
