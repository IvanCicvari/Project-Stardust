-- Check if the database exists and create it if not
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'Stardust')
BEGIN
    CREATE DATABASE Stardust;
END
GO

-- Switch to the database
USE Stardust;
GO

-- Create Users Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Users')
BEGIN
    CREATE TABLE Users (
        IDUser INT PRIMARY KEY IDENTITY(1,1),
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        UserName VARCHAR(50) UNIQUE,
        Email VARCHAR(100) UNIQUE,
        Password VARCHAR(255),
        CountryID INT,
        CityID INT,
        CoordinatesID INT,
        RolesID INT,
        FOREIGN KEY (CountryID) REFERENCES Country(IDCountry),
        FOREIGN KEY (CityID) REFERENCES City(IDCity),
        FOREIGN KEY (CoordinatesID) REFERENCES Coordinates(IDCoordinates),
        FOREIGN KEY (RolesID) REFERENCES User_Roles(IDRole)
    );
END
GO

-- Create Stores Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Stores')
BEGIN
    CREATE TABLE Stores (
        IDStore INT PRIMARY KEY IDENTITY(1,1),
        NameOfStore VARCHAR(100),
        CoordinatesID INT,
        ChainID INT,
        FOREIGN KEY (CoordinatesID) REFERENCES Coordinates(IDCoordinates),
        FOREIGN KEY (ChainID) REFERENCES Chains(IDChain)
    );
END
GO

-- Create Items Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Items')
BEGIN
    CREATE TABLE Items (
        IDItems INT PRIMARY KEY IDENTITY(1,1),
        NameOfItem VARCHAR(100),
        Price DECIMAL(10, 2),
        ImageURL VARCHAR(255)
    );
END
GO

-- Create Country Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Country')
BEGIN
    CREATE TABLE Country (
        IDCountry INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR(100)
    );
END
GO

-- Create City Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'City')
BEGIN
    CREATE TABLE City (
        IDCity INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR(100),
        CountryID INT,
        FOREIGN KEY (CountryID) REFERENCES Country(IDCountry)
    );
END
GO

-- Create Coordinates Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Coordinates')
BEGIN
    CREATE TABLE Coordinates (
        IDCoordinates INT PRIMARY KEY IDENTITY(1,1),
        Latitude DECIMAL(9, 6),
        Longitude DECIMAL(9, 6)
    );
END
GO

-- Create Chains Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Chains')
BEGIN
    CREATE TABLE Chains (
        IDChain INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR(100)
    );
END
GO

-- Create Item_Store Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Item_Store')
BEGIN
    CREATE TABLE Item_Store (
        StoreID INT,
        ItemID INT,
        PRIMARY KEY (StoreID, ItemID),
        FOREIGN KEY (StoreID) REFERENCES Stores(IDStore),
        FOREIGN KEY (ItemID) REFERENCES Items(IDItems)
    );
END
GO

-- Create Favorites Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Favorites')
BEGIN
    CREATE TABLE Favorites (
        UserID INT,
        StoreID INT,
        PRIMARY KEY (UserID, StoreID),
        FOREIGN KEY (UserID) REFERENCES Users(IDUser),
        FOREIGN KEY (StoreID) REFERENCES Stores(IDStore)
    );
END
GO

-- Create Audit_Log Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Audit_Log')
BEGIN
    CREATE TABLE Audit_Log (
        IDLog INT PRIMARY KEY IDENTITY(1,1),
        UserID INT,
        Action VARCHAR(255),
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES Users(IDUser)
    );
END
GO

-- Create User_Roles Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'User_Roles')
BEGIN
    CREATE TABLE User_Roles (
        IDRole INT PRIMARY KEY IDENTITY(1,1),
        RoleName VARCHAR(50)
    );
END
GO

-- Create User_Role_Assignments Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'User_Role_Assignments')
BEGIN
    CREATE TABLE User_Role_Assignments (
        UserID INT,
        RoleID INT,
        PRIMARY KEY (UserID, RoleID),
        FOREIGN KEY (UserID) REFERENCES Users(IDUser),
        FOREIGN KEY (RoleID) REFERENCES User_Roles(IDRole)
    );
END
GO

-- Create Recommendations Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Recommendations')
BEGIN
    CREATE TABLE Recommendations (
        IDRecommendation INT PRIMARY KEY IDENTITY(1,1),
        ItemID INT,
        FOREIGN KEY (ItemID) REFERENCES Items(IDItems)
    );
END
GO

-- Create Comments Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Comments')
BEGIN
    CREATE TABLE Comments (
        IDComment INT PRIMARY KEY IDENTITY(1,1),
        Text TEXT,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        UserID INT,
        FOREIGN KEY (UserID) REFERENCES Users(IDUser)
    );
END
GO

-- Create Promotions Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Promotions')
BEGIN
    CREATE TABLE Promotions (
        IDPromotion INT PRIMARY KEY IDENTITY(1,1),
        StoreID INT,
        ItemID INT,
        Description TEXT,
        StartDate DATE,
        EndDate DATE,
        DiscountPercentage DECIMAL(5, 2),
        FOREIGN KEY (StoreID) REFERENCES Stores(IDStore),
        FOREIGN KEY (ItemID) REFERENCES Items(IDItems)
    );
END
GO

-- Create Reviews Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Reviews')
BEGIN
    CREATE TABLE Reviews (
        IDReview INT PRIMARY KEY IDENTITY(1,1),
        UserID INT,
        StoreID INT,
        ItemID INT,
        Rating INT,
        Text TEXT,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES Users(IDUser),
        FOREIGN KEY (StoreID) REFERENCES Stores(IDStore),
        FOREIGN KEY (ItemID) REFERENCES Items(IDItems)
    );
END
GO

-- Create Store_Hours Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Store_Hours')
BEGIN
    CREATE TABLE Store_Hours (
        IDStoreHours INT PRIMARY KEY IDENTITY(1,1),
        StoreID INT,
        DayOfWeek VARCHAR(10),
        OpeningTime TIME,
        ClosingTime TIME,
        FOREIGN KEY (StoreID) REFERENCES Stores(IDStore)
    );
END
GO

-- Create Notifications Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Notifications')
BEGIN
    CREATE TABLE Notifications (
        IDNotification INT PRIMARY KEY IDENTITY(1,1),
        UserID INT,
        Title VARCHAR(100),
        Message TEXT,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        IsRead BIT DEFAULT 0,
        FOREIGN KEY (UserID) REFERENCES Users(IDUser)
    );
END
GO

-- Create Wishlist Table
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Wishlist')
BEGIN
    CREATE TABLE Wishlist (
        IDWishlist INT PRIMARY KEY IDENTITY(1,1),
        UserID INT,
        ItemID INT,
        FOREIGN KEY (UserID) REFERENCES Users(IDUser),
        FOREIGN KEY (ItemID) REFERENCES Items(IDItems)
    );
END
GO

