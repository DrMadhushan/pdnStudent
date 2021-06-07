import { Student } from './../../student.model';
import { AuthService } from './auth.service';
import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/database';
import firebase from 'firebase/app';
import 'firebase/database';




@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  requiredUserId:any;
  studentData:any;
  public student: Student;

  constructor(private db: AngularFireDatabase, private authService: AuthService) { 
    this.student = new Student;
  }

  setRequiredUserId(user:String){
    this.requiredUserId = user;
    // return requested user's Id
  }

  getUserViewData(){
    let userId = this.authService.getCurrentUser();
    const dbRef = firebase.database().ref();
    dbRef.child("Students").child(userId).get().then((snapshot) => {
      if (snapshot.exists()) {
        let x = snapshot.val();
        this.student.displayName = x.displayName;
        this.student.email = x.personalEmail;
        this.student.phoneNumber = x.phoneNo;
        console.log("User detected in database service: "+snapshot.val().displayName);
      } else {console.log("No data available");} }).catch((error) => {console.error(error);});
    
    dbRef.child("UniData").child(userId).get().then((snapshot) => {
      if (snapshot.exists()) {
        let x = snapshot.val();
        this.student.batch = x.batch;
        this.student.faculty = x.faculty;
        this.student.dob = x.dob;
        this.student.firstName = x.firstName;
        this.student.lastName = x.lastName;
        this.student.gender = x.gender;
        console.log(snapshot.val());
      } else {console.log("No data available");} }).catch((error) => {console.error(error);});
      
      /*dbRef.child("BlogLinks").child(userId).get().then((snapshot) =>{
        if (snapshot.exists()) {
          let returnArr:any[] = [];

          snapshot.forEach(function(childSnapshot) {
              var item = childSnapshot.val();
              item.key = childSnapshot.key;
      
              returnArr.push(item);
          })
          this.student.blogs = returnArr;
        } else {console.log("No data available");} }).catch((error) => {console.error(error);});
    */
        return this.student;
  }

  showMyProfile(){
    // return my userId
  }



}
