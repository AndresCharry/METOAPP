import math

def geo_to_ECEF(lat, log, H):
    # Convert lat, long, height in WGS84 to ECEF X,Y,Z
    # lat and long given in decimal degrees.
    # altitude should be given in meters
    lat = float(lat)
    log = float(log)
    H = float(H)
    lat = math.radians(lat)        # converting to radians
    log = math.radians(log)        # converting to radians
    a = 6378137.0                  # earth semimajor axis in meters
    f = 1/298.257223563            # reciprocal flattening
    e2 = 2*f - f**2                # eccentricity squared
    
    chi = math.sqrt(1-e2*(math.sin(lat))**2)
    X = (a/chi + H)*math.cos(lat)*math.cos(log)
    Y = (a/chi + H)*math.cos(lat)*math.sin(log)
    Z = (a*(1-e2)/chi + H)*math.sin(lat)

    return X, Y, Z

def ECEF_to_ENU(lat_0, log_0, H0, X, Y, Z):
    # convert ECEF coordinates to local east, north, up
 
    # find reference location in ECEF coordinates
    lat_0 = float(lat_0)
    log_0 = float(log_0)
    H0 = float(H0)
    Xr,Yr,Zr = geo_to_ECEF(lat_0, log_0, H0)  #location of reference point
 
    e = -math.sin(log_0)*(X-Xr) + math.cos(log_0)*(Y-Yr)
    n = -math.sin(lat_0)*math.cos(log_0)*(X-Xr) - math.sin(lat_0)*math.sin(log_0)*(Y-Yr) + math.cos(lat_0)*(Z-Zr)
    u = math.cos(lat_0)*math.cos(log_0)*(X-Xr) + math.cos(lat_0)*math.sin(log_0)*(Y-Yr) + math.sin(lat_0)*(Z-Zr)

    return e,n,u

def ENU_TO_ECEF(lat_0, log_0, H0, E, N, U):
    # Convert east, north, up coordinates (labeled e, n, u) to ECEF
    # coordinates. The reference point (phi, lambda, h) must be given. All distances are in metres
 
    Xr,Yr,Zr = geo_to_ECEF(lat_0, log_0, H0) #location of reference point
    X = -math.sin(lat_0)*E - math.cos(log_0)*math.sin(lat_0)*N + math.cos(log_0)*math.cos(lat_0)*U + Xr
    Y = math.cos(log_0)*E - math.sin(log_0)*math.sin(lat_0)*N + math.cos(lat_0)*math.sin(log_0)*U + Yr
    Z = math.cos(lat_0)*N + math.sin(lat_0)*U + Zr

    return X, Y, Z

def ECEF_to_geo(X,Y,Z):

    a = 6378137.0 # earth semimajor axis in meters
    f = 1/298.257223563 #reciprocal flattening
    b = a*(1-f) #semi-minor axis
    
    e2 = 2*f-f**2 #first eccentricity squared
    ep2 = f*(2-f)/((1-f)**2)  #second eccentricity squared
    
    r2 = X**2 + Y**2
    r = math.sqrt(r2)
    E2 = a**2 - b**2
    F = 54*b**2*Z**2
    G = r2 + (1-e2)*Z**2 - e2*E2
    c = (e2**2*F*r2)/(G**3)
    s = ( 1 + c + math.sqrt(c**2 + 2*c))**(1/3)
    P = F/(3*(s+1/s+1)**2*G**2)
    Q = math.sqrt(1+2*e2**2*P)
    ro = -(e2*P*r)/(1+Q) + math.sqrt((a**2/2)*(1+1/Q) - ((1-e2)*P*Z**2)/(Q*(1+Q)) - P*r2/2)
    tmp = (r - e2*ro)**2
    U = math.sqrt( tmp + Z**2 )
    V = math.sqrt( tmp + (1-e2)*Z**2 )
    zo = (b**2*Z)/(a*V)
    
    H = U*( 1 - b**2/(a*V))
    lat = math.degrees(math.atan( (Z + ep2*zo)/r ))
    log = math.degrees(math.atan2(Y,X))

    return lat, log, H

if __name__ == '__main__':
    lat = 4.43807
    log = -75.19964
    h = 1000

     # geo to ecef
    ECEF = geo_to_ECEF(lat, log, h)
    print(ECEF)
     # ecef to enu
    ENU = ECEF_to_ENU(lat, log, h, ECEF[0], ECEF[1], ECEF[2])
    print(ENU)

    # enu to ecef
    ECEF = ENU_TO_ECEF(lat, log, h, ENU[0], ENU[1], ENU[2])
    print(ECEF)
    # ecef to geo
    GEO = ECEF_to_geo(ECEF[0], ECEF[1], ECEF[2])
    print(GEO)