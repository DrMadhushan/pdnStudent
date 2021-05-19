import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EduBlockComponent } from './stu-info.component';

describe('EduBlockComponent', () => {
  let component: EduBlockComponent;
  let fixture: ComponentFixture<EduBlockComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EduBlockComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EduBlockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
