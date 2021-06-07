import { environment } from './../environments/environment.prod';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AngularFireModule } from "@angular/fire";
import { AngularFireAuthModule } from "@angular/fire/auth";
import { AngularFirestoreModule } from '@angular/fire/firestore';
import { FormsModule } from '@angular/forms';
import { AngularFireDatabaseModule } from '@angular/fire/database';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MdbModule } from 'mdb-angular-ui-kit';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { StudentDetailsComponent } from './student-details/student-details.component';
import { ProfileCardComponent } from './profile-card/profile-card.component';
import { EduSectionComponent } from './stu-info-collection/stu-info-collection.component';
import { EduBlockComponent } from './stu-info/stu-info.component';
import { InterestsComponent } from './interests/interests.component';
import { InterestComponent } from './interest/interest.component';
import { BlogPostComponent } from './blog-post/blog-post.component';
import { BlogCollectionComponent } from './blog-collection/blog-collection.component';
import { StudentProfileComponent } from './student-profile/student-profile.component';
import { FooterComponent } from './footer/footer.component';
import { SigninComponent } from './signin/signin.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { EditImageComponent } from './edit-profile/edit-image/edit-image.component';
import { EditNameComponent } from './edit-profile/edit-name/edit-name.component';
import { EditBioComponent } from './edit-profile/edit-bio/edit-bio.component';
import { EditSocialComponent } from './edit-profile/edit-social/edit-social.component';
import { EditBlogComponent } from './edit-profile/edit-blog/edit-blog.component';
import { EditEducationComponent } from './edit-profile/edit-education/edit-education.component';
import { EditExperienceComponent } from './edit-profile/edit-experience/edit-experience.component';
import { EditSkillsComponent } from './edit-profile/edit-skills/edit-skills.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { LogoMainComponent } from './logo-main/logo-main.component';
import { NgForm } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    StudentDetailsComponent,
    ProfileCardComponent,
    EduSectionComponent,
    EduBlockComponent,
    InterestsComponent,
    InterestComponent,
    BlogPostComponent,
    BlogCollectionComponent,
    StudentProfileComponent,
    FooterComponent,
    SigninComponent,
    EditProfileComponent,
    EditImageComponent,
    EditNameComponent,
    EditBioComponent,
    EditSocialComponent,
    EditBlogComponent,
    EditEducationComponent,
    EditExperienceComponent,
    EditSkillsComponent,
    HomeComponent,
    PageNotFoundComponent,
    ResetPasswordComponent,
    LogoMainComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MdbModule,
    BrowserAnimationsModule,
    RouterModule,
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireAuthModule,
    AngularFirestoreModule,
    FormsModule,
    AngularFireDatabaseModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
