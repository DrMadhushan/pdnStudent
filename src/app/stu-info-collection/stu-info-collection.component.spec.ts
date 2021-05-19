import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EduSectionComponent } from './stu-info-collection.component';

describe('EduSectionComponent', () => {
  let component: EduSectionComponent;
  let fixture: ComponentFixture<EduSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EduSectionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EduSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
