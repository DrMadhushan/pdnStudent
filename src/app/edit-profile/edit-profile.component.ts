import { RouteResolver } from './../resolvers/route.resolver';
import { Student } from './../student.model';
import { DatabaseService } from './../shared/services/database.service';
import { AuthService } from './../shared/services/auth.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth';
AuthService
@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss']
})
export class EditProfileComponent implements OnInit {
  profileImg:string = "assets/img/profile-pic1.jpg";
  userId:any = "guest";
  isLoggedIn:boolean = false;
  userData:any;
  name: String | any;
  curStudent: Student;
  
  constructor(
    public router: Router, 
    public authService: AuthService, 
    private db: DatabaseService,
    private activatdRoute: ActivatedRoute,
    private routeResover: RouteResolver) {
    localStorage.setItem('user',this.authService.getCurrentUser());
  }

  ngOnInit(): void {
    this.userId = localStorage.getItem('user');
    let promise = new Promise((resolve, reject) => {
      console.log(this.fetchData(this.userId).email);
      return this.fetchData(this.userId);
    }).then(value => {
      console.log("value is: ", value);
      console.log("inside new promise: "+this.curStudent.getDisplayName());
    })
    
    
    this.activatdRoute.data.subscribe(data => {
      console.log(this.curStudent.getDisplayName());
      console.log("user is: "+localStorage.getItem('user'));
      //console.log(data[0].displayName);
      if(localStorage.getItem('user') != 'guest'){
        this.isLoggedIn = true;
        this.userId = localStorage.getItem('user');
        
        this.name = data.displayName;
        console.log("User Name is: "+this.name);
      }
      else{
        this.router.navigateByUrl('signin');
      }

    })
    
  }

  /*ngOnChanges(): void{
    this.userId = console.log(localStorage.getItem('user'));
    if (this.userId == 'guest'){
      this.router.navigateByUrl('signin');
    }
  }*/

  showUser(){
    // var u = {"user":{"uid":"4grjzp0BBZR8GzhRKoXEnUF4YWp1","displayName":null,"photoURL":null,"email":"drmadhushan@gmail.com","emailVerified":false,"phoneNumber":null,"isAnonymous":false,"tenantId":null,"providerData":[{"uid":"drmadhushan@gmail.com","displayName":null,"photoURL":null,"email":"drmadhushan@gmail.com","phoneNumber":null,"providerId":"password"}],"apiKey":"AIzaSyDdr7GRkFRaA9dIBxzgcGBouMUzAIyk69g","appName":"[DEFAULT]","authDomain":"pdnstudent-temp.firebaseapp.com","stsTokenManager":{"apiKey":"AIzaSyDdr7GRkFRaA9dIBxzgcGBouMUzAIyk69g","refreshToken":"AGEhc0DJj5uUKF46OYokL3bDYHKGA82ddZsLkNMswELZ202pvkBpPhQbJG14Xkyj1coIP_gPzSr9YAmnsHd42WRVfWiE-wKev_QWJkfGDxBA772wCi-yeLbQX1EvtPR6i1wPlWv27En5OjFVoh2CIPqxazfbIxRSGJUE7qcaAYOYLo7Qcv5mx11Ggatsg38PDxON7d17sv6902YRybLYxuzN2hA29MKQhg","accessToken":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzNmRhZWFiZjhkZDY1ZDRkZTIxZTgyNGI4OTlhMWYzZGEyZjg5NTgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGRuc3R1ZGVudC10ZW1wIiwiYXVkIjoicGRuc3R1ZGVudC10ZW1wIiwiYXV0aF90aW1lIjoxNjIxMTExNzI2LCJ1c2VyX2lkIjoiNGdyanpwMEJCWlI4R3poUktvWEVuVUY0WVdwMSIsInN1YiI6IjRncmp6cDBCQlpSOEd6aFJLb1hFblVGNFlXcDEiLCJpYXQiOjE2MjExMTE3MjYsImV4cCI6MTYyMTExNTMyNiwiZW1haWwiOiJkcm1hZGh1c2hhbkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZHJtYWRodXNoYW5AZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.apTjlbetWl8JXo498L0gg2C5W3jdlCl5VmRZRUqHpHU3upP0ofLId7NphVXoA_bbkEGQYTuxKwEsm-8rVLJbc17pWKz2Ry_czW45QTJsq-UZVe3XXUJzNtAw4zAmukGbixIM3bigYbJfYvVjYglbGJsOa4AmibyJug4vc_KHu_PF62PZJrcJ1SRwoZrOPx0HddHw_Sck_myV_BmPgZE3rLnS8lKWNxwps-oEcgnb136TECczvvSl37vNRaLhKpZmhPfmTlgovW5q8iai4U8ikT7rCI7gyHVsfllnuv1WYpqj6aYhLsU3cUkUD1igzu6zZc4HsszotTmI_E_X5pnztw","expirationTime":1621115326981},"redirectEventId":null,"lastLoginAt":"1621111663310","createdAt":"1621102465280","multiFactor":{"enrolledFactors":[]}},"credential":null,"additionalUserInfo":{"providerId":"password","isNewUser":false},"operationType":"signIn"}
    
    console.log("Current user is: ", this.userData['user']['uid']);
    this.viewProfile();
    
  }

  viewProfile(){
    // this.db.getUserViewData();
    // this.router.navigateByUrl('student-profile');
  }

  fetchData(userId:any){
    // this.db.setRequiredUserId(this.userId);
    this.curStudent = this.db.getUserViewData();
    return this.curStudent;
  }

  getDisplayName(){
    return this.db.student.displayName;
  }
}
