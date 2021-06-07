export class Student{
  email:any;
  nic:any;
  password:any;
  displayName: any | null;
  firstName:any;
  lastName:any;
  district:any;
  faculty:any;
  department:any;
  eNumber:any;
  batch:any;
  dob:any;
  gender:any;
  phoneNumber:any;
  blogs:any[] | undefined;
  skills:any[] | undefined;
  socialLinks:any[] | undefined;
  academics:any[] | undefined;
  experiences:any[] | undefined;

  getDisplayName(){
    return this.displayName;
  }
}

/*
export class Student{
    email:String | undefined;
    nic:String | undefined;
    password:any;
    firstName:String | undefined;
    lastName:String;
    district:String;
    faculty:String;
    department:String;
    eNumber:String;
    batch:String;
    dob:String;
    gender:String;
    phoneNumber:String;
    blogs:any[];
    skills:any[];
    socialLinks:any[];
    academics:any[];
    experiences:any[];

  
    constructor(init?:Partial<Student>){
      Object.assign(this, init);
    }

    setStudentAcademicData(academics:any[]){ this.academics = academics; }
    setStudentSocialData(socialLinks:any[]){ this.socialLinks = socialLinks; }
    setStudentBlogs(blogs:any[]){ this.blogs = blogs; }
    setStudentSkills(skills:any[]){ this.skills = skills; }

    public setUserBasicData(dArr:any){
      this.email = dArr[0];
      this.nic = dArr[1];
      this.password = this.nic;
      this.firstName = dArr[2];
      this.lastName = dArr[3];
      this.district = dArr[4];
      this.faculty = dArr[5];
      this.department = dArr[6];
      this.eNumber = dArr[7];
      this.batch = dArr[8];
      this.dob = dArr[9];
      this.gender = dArr[10];
      this.phoneNumber = dArr[11];
    }

  }
  */