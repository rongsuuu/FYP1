from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.sqlite import FLOAT, INTEGER, VARCHAR


Base = declarative_base()

class ENR2_1table(Base):
    __tablename__ = 'ENR2_1'
    id = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR(length=1024))
    Lateral_limits_information = Column(VARCHAR(length=1024))
    Lateral_Limit_id = Column(INTEGER, ForeignKey('ENR2_1_Lateral_Limits.Lateral_Limit_id'))
    Upper_limit = Column(VARCHAR(length=1024))
    Lower_limit = Column(VARCHAR(length=1024))
    class_of_airspace = Column(VARCHAR(length=1024))
    Unit_providing_service = Column(VARCHAR(length=1024))
    Remarks = Column(VARCHAR(length=1024))

class ENR2_1_Lateral_Limitstable(Base):
    __tablename__ = 'ENR2_1_Lateral_Limits'
    id = Column(INTEGER, primary_key=True)
    Lateral_Limit_id = Column(INTEGER)
    Lateral_Limit_Latitude = Column(FLOAT)
    Lateral_Limit_Longitude = Column(FLOAT)

class ENR3_1_1maintable(Base):
    __tablename__ = 'ENR3_1_1main'
    id = Column(INTEGER, primary_key=True)
    Route_Designator = Column(VARCHAR(length=1024))
    Route_Usage_Notes = Column(VARCHAR(length=1024))

class ENR3_1_2joiningtable(Base):
    __tablename__ = 'ENR3_1_2joining'
    id = Column(INTEGER, primary_key=True)
    ATS_id = Column(INTEGER, ForeignKey('ENR3_1_1main.id'))
    Segment_id = Column(INTEGER, ForeignKey('ENR3_1_3Segment.s_id'))

class ENR3_1_3Segmenttable(Base):
    __tablename__ = 'ENR3_1_3Segment'
    s_id = Column(INTEGER, primary_key=True)
    start = Column(INTEGER, ForeignKey('ENR3_1_4Significantpoints.startend_id'))
    end = Column(INTEGER, ForeignKey('ENR3_1_4Significantpoints.startend_id'))
    Track_MAG_down = Column(VARCHAR(length=1024))
    Track_MAG_up = Column(VARCHAR(length=1024))
    Dist_NM = Column(VARCHAR(length=1024))
    Upper_limit = Column(VARCHAR(length=1024))
    Lower_limit = Column(VARCHAR(length=1024))
    MNM_FT_ALT = Column(VARCHAR(length=1024))
    Lateral_limits_NM = Column(INTEGER)
    FL_down = Column(VARCHAR(length=1024))
    FL_up = Column(VARCHAR(length=1024))
    Remarks = Column(VARCHAR(length=1024))

class ENR3_1_Signpointtable(Base):
    __tablename__ = 'ENR3_1_4Significantpoints'
    startend_id = Column(INTEGER, primary_key=True)
    Route_Designator = Column(VARCHAR(length=1024))
    Significant_point_name = Column(VARCHAR(length=1024))
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)

class ENR3_3_1maintable(Base):
    __tablename__ = 'ENR3_3_1main'
    id = Column(INTEGER, primary_key=True)
    Route_Designator = Column(VARCHAR(length=1024))
    Route_Usage_Notes = Column(VARCHAR(length=1024))

class ENR3_3_2table(Base):
    __tablename__ = 'ENR3_3_2'
    id = Column(INTEGER, primary_key=True)
    ATS_id = Column(INTEGER, ForeignKey('ENR3_3_1main.id'))
    Segment_id = Column(INTEGER, ForeignKey('ENR3_3_3Segment.s_id'))

class ENR3_3_3Segmenttable(Base):
    __tablename__ = 'ENR3_3_3Segment'
    s_id = Column(INTEGER, primary_key=True)
    start = Column(INTEGER, ForeignKey('ENR3_3_4Significantpoints.startend_id'))
    end = Column(INTEGER, ForeignKey('ENR3_3_4Significantpoints.startend_id'))
    Track_MAG_down = Column(VARCHAR(length=1024))
    Track_MAG_up = Column(VARCHAR(length=1024))
    Great_Circle_Dist_NM = Column(VARCHAR(length=1024))
    Upper_limit = Column(VARCHAR(length=1024))
    Lower_limit = Column(VARCHAR(length=1024))
    FL_down = Column(VARCHAR(length=1024))
    FL_up = Column(VARCHAR(length=1024))
    Remarks = Column(VARCHAR(length=1024))

class ENR3_3_Signpointtable(Base):
    __tablename__ = 'ENR3_3_4Significantpoints'
    startend_id = Column(INTEGER, primary_key=True)
    Route_Designator = Column(VARCHAR(length=1024))
    Significant_point_name = Column(VARCHAR(length=1024))
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)

class ENR3_6table(Base):
    __tablename__ = 'ENR3_6'
    Id = Column(INTEGER, primary_key=True)
    HLGD_ID = Column(VARCHAR(length=1024))
    FIX = Column(VARCHAR(length=1024))
    WPT_Coordinates_latitude = Column(FLOAT)
    WPT_Coordinates_longitude = Column(FLOAT)
    INBD_TR = Column(INTEGER)
    Direction_of_Procedure_Turn = Column(VARCHAR(length=1024))
    MAX_IAS = Column(VARCHAR(length=1024))
    MNM_MAX = Column(VARCHAR(length=1024))
    HLDG_Level = Column(VARCHAR(length=1024))
    Time = Column(FLOAT)
    Controlling_Unit_and_Frequency = Column(VARCHAR(length=1024))

class ENR4_1table(Base):
    __tablename__ = 'ENR4_1'
    Id_no = Column(INTEGER,primary_key=True)
    Name_of_station = Column(VARCHAR(length=1024))
    Id = Column(VARCHAR(length=1024))
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)
    Frequency = Column(VARCHAR(length=1024))
    ELEV_DME_antenna = Column(VARCHAR(length=1024))
    Hours_of_operation = Column(VARCHAR(length=1024))
    Remark = Column(VARCHAR(length=1024))

class ENR4_4table(Base):
    __tablename__ = 'ENR4_4'
    Id = Column(INTEGER,primary_key=True)
    Name_Code_designator = Column(VARCHAR(length=1024))
    Longitude = Column(FLOAT)
    Latitude = Column(FLOAT)
    ATS_route_or_other_route = Column(VARCHAR(length=1024))
    Terminal_Area = Column(VARCHAR(length=1024))

class ENR4_5table(Base):
    __tablename__ = 'ENR4_5'
    Id = Column(INTEGER,primary_key=True)
    Name_Ident_coordinates = Column(VARCHAR(length=1024))
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)
    Type_and_Intensity = Column(VARCHAR(length=1024))
    Characteristics = Column(VARCHAR(length=1024))
    Operating_Hours = Column(VARCHAR(length=1024))
    Remark = Column(VARCHAR(length=1024))

class ENR5_1table(Base):
    __tablename__ = 'ENR5_1'
    id = Column(INTEGER, primary_key=True)
    Information = Column(VARCHAR(length=1024))
    Lateral_Limit_id = Column(INTEGER, ForeignKey('ENR5_1_Lateral_Limits.Lateral_Limit_id'))
    Identification = Column(VARCHAR(length=1024))
    Name = Column(VARCHAR(length=1024))
    Lateral_Limits = Column(VARCHAR(length=1024))
    Upper_limit = Column(VARCHAR(length=1024))
    Lower_limit = Column(VARCHAR(length=1024))
    Remarks = Column(VARCHAR(length=1024))

class ENR5_1_Lateral_Limitstable(Base):
    __tablename__ = 'ENR5_1_Lateral_Limits'
    id = Column(INTEGER, primary_key=True)
    Lateral_Limit_id = Column(INTEGER)
    Lateral_Limit_Latitude = Column(FLOAT)
    Lateral_Limit_Longitude = Column(FLOAT)

class ENR5_2table(Base):
    __tablename__ = 'ENR5_2'
    Id = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR(length=1024))
    Lateral_Limit_Latitude = Column(FLOAT)
    Lateral_Limit_Longitude = Column(FLOAT)
    Remark = Column(VARCHAR(length=1024))
    Upper_Limi_Lower_Limit = Column(VARCHAR(length=1024))
    Remarks_Time_of_Act = Column(VARCHAR(length=1024))


class ENR3_ATS_ROUTES_table(Base):
    __tablename__ = 'ENR3_ATS_ROUTES'
    id = Column(INTEGER, primary_key=True)
    Route_Designator = Column(VARCHAR(length=1024))
    Significant_point_name = Column(VARCHAR(length=1024))
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)


