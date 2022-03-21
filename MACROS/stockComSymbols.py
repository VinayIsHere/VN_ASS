import enum
class StockSymbols(enum.Enum):
    Adani_Port_and_Special_Economic_Zone=1
    Asian_Paints_Ltd=2;
    Axis_Bank_Ltd=3;
    Bajaj_Auto_Ltd=4;
    Bajaj_Finance_Ltd=5;
    Bharat_Petroleum_Corporation_Ltd=6;
    Bhart_Infratel_Ltd=7;
    Cipla_Ltd=8;
    Coal_India_Ltd=9;
    Dr_Reddys_Laboratories_Ltd=10;

    Eicher_Motors_Ltd=11;
    Gail_Ltd=12;
    Grasim_Industries_Ltd=13;
    Hcl_Technologies_Ltd=14;
    HDFC_Bank_Ltd=15;
    Hero_MotoCorp_Ltd=16;
    Hindalco_industries_Ltd=17;
    Hindustan_Petroleum_Corporation_Ltd=18;
    Hindustan_Unilever_Ltd=19;
    Housing_Development_Finance_Corporation_Ltd=20;

    ITC_Ltd=21;
    ICICI_Bank=22;
    Indiabulls_Housing_Finance_Ltd=23;
    Indian_Oil_corporation_Ltd=24;
    Induslnd_Bank_Ltd=25;
    Infosys_Ltd=26;
    Kotak_Mahindra_Bank_Ltd=27;
    Larsen_And_Toubro_Ltd=28;
    Lupin_Ltd=29;
    Mahindra_And_Mahindra_Ltd=30;

    Maruti_Suzuki_India_Ltd=31;
    NTPC_Ltd=32;
    Oil_And_Natural_Gas_Corporation_Ltd=33;
    Power_Grid_Corporation_Ltd=34;
    Relience_Insdustries_Ltd=35;
    State_Bank_Of_India=36;
    Sun_Pharmaceutical_Industries_Ltd=37;
    Tata_Consultancy_Services_Ltd=38;
    Tata_Motor_Ltd=39;
    METALS=40;

    Tech_Mahindra_Ltd=41;
    Titan_Company_Ltd=42;
    UPL_Ltd=43;
    UltraTech_Cement_Ltd=44;
    Venanta_Ltd=45;
    Wipro_Ltd=46;
    Yes_Bank_Ltd=47;
    Zee_Entertainment_Enterprises_Ltd=48;

symbols={
    StockSymbols.Adani_Port_and_Special_Economic_Zone:'ASIANPAINT',
    StockSymbols.Asian_Paints_Ltd:"ASIANPAINT",
    StockSymbols.Axis_Bank_Ltd:"AXISBANK",
    StockSymbols.Bajaj_Auto_Ltd:"BAJAJ-AUTO",
    StockSymbols.Bajaj_Finance_Ltd:"BAJFINANCE",
    StockSymbols.Bharat_Petroleum_Corporation_Ltd:"BPCL",
    StockSymbols.Bhart_Infratel_Ltd:"INFRATEL",
    StockSymbols.Cipla_Ltd:"CIPLA",
    StockSymbols.Coal_India_Ltd:"COALINDIA",
    StockSymbols.Dr_Reddys_Laboratories_Ltd:"DRREDDY",

    StockSymbols.Eicher_Motors_Ltd:"EICHERMOT",
    StockSymbols.Gail_Ltd:"GAIL",
    StockSymbols.Grasim_Industries_Ltd:"GRASIM",
    StockSymbols.Hcl_Technologies_Ltd:"HCLTECH",
    StockSymbols.HDFC_Bank_Ltd:"HDFCBANK",
    StockSymbols.Hero_MotoCorp_Ltd:"HEROMOTOCO",
    StockSymbols.Hindalco_industries_Ltd:"HINDALCO",
    StockSymbols.Hindustan_Petroleum_Corporation_Ltd:"HINDPETRO",
    StockSymbols.Hindustan_Unilever_Ltd:"HINDUNILVR",
    StockSymbols.Housing_Development_Finance_Corporation_Ltd:"HDFC",

    StockSymbols.ITC_Ltd:"ITC",
    StockSymbols.ICICI_Bank:"ICICIBANK",
    StockSymbols.Indiabulls_Housing_Finance_Ltd:"IBULHSGFIN",
    StockSymbols.Indian_Oil_corporation_Ltd:"IOC",
    StockSymbols.Induslnd_Bank_Ltd:"INDUSINDBK",
    StockSymbols.Infosys_Ltd:"INFY",
    StockSymbols.Kotak_Mahindra_Bank_Ltd:"KOTAKBANK",
    StockSymbols.Larsen_And_Toubro_Ltd:"LT",
    StockSymbols.Lupin_Ltd:"LUPIN",
    StockSymbols.Mahindra_And_Mahindra_Ltd:"M&M",

    StockSymbols.Maruti_Suzuki_India_Ltd:"MARUTI",
    StockSymbols.NTPC_Ltd:"NTPC",
    StockSymbols.Oil_And_Natural_Gas_Corporation_Ltd:"ONGC",
    StockSymbols.Power_Grid_Corporation_Ltd:"POWERGRID",
    StockSymbols.Relience_Insdustries_Ltd:"RELIANCE",
    StockSymbols.State_Bank_Of_India:"SBIN",
    StockSymbols.Sun_Pharmaceutical_Industries_Ltd:"SUNPHARMA",
    StockSymbols.Tata_Consultancy_Services_Ltd:"TCS",
    StockSymbols.Tata_Motor_Ltd:"TATAMOTORS",
    StockSymbols.METALS:"TATASTEEL",

    StockSymbols.Tech_Mahindra_Ltd:"TECHM",
    StockSymbols.Titan_Company_Ltd:"TITAN",
    StockSymbols.UPL_Ltd:"UPL",
    StockSymbols.UltraTech_Cement_Ltd:"ULTRACEMCO",
    StockSymbols.Venanta_Ltd:"VEDL",
    StockSymbols.Wipro_Ltd:"WIPRO",
    StockSymbols.Yes_Bank_Ltd:"YESBANK",
    StockSymbols.Zee_Entertainment_Enterprises_Ltd:"ZEEL"};



# symbol={"Adani_Port_and_Special_Economic_Zone":'ASIANPAINT',
#     "Asian_Paints_Ltd":"ASIANPAINT",
#     "Axis_Bank_Ltd":"AXISBANK",
#     "Bajaj_Auto_Ltd":"BAJAJ-AUTO",
#     "Bajaj_Finance_Ltd":"BAJFINANCE",
#     "Bharat_Petroleum_Corporation_Ltd":"BPCL",
#     "Bhart_Infratel_Ltd":"INFRATEL",
#     "Cipla_Ltd":"CIPLA",
#     "Coal_India_Ltd":"COALINDIA",
#     "Dr_Reddys_Laboratories_Ltd":"DRREDDY",
#     "Eicher_Motors_Ltd":"EICHERMOT",
#     "Gail_Ltd":"GAIL",
#     "Grasim_Industries_Ltd":"GRASIM",
#     "Hcl_Technologies_Ltd":"HCLTECH",
#     "HDFC_Bank_Ltd":"HDFCBANK",
#     "Hero_MotoCorp_Ltd":"HEROMOTOCO",
#     "Hindalco_industries_Ltd":"HINDALCO",
#     "Hindustan_Petroleum_Corporation_Ltd":"HINDPETRO",
#     "Hindustan_Unilever_Ltd":"HINDUNILVR",
#     "Housing_Development_Finance_Corporation_Ltd":"HDFC",
#     "ITC_Ltd":"ITC",
#     "ICICI_Bank":"ICICIBANK",
#     "Indiabulls_Housing_Finance_Ltd ":"IBULHSGFIN",
#     "Indian_Oil_corporation_Ltd":"IOC",
#     "Induslnd_Bank_Ltd":"INDUSINDBK",
#     "Infosys_Ltd":"INFY",
#     "Kotak_Mahindra_Bank_Ltd":"KOTAKBANK",
#     "Larsen_And_Toubro_Ltd":"LT",
#     "Lupin_Ltd":"LUPIN",
#     "Mahindra_And_Mahindra_Ltd":"M&M"};

class micros(enum.Enum):
    multiplier=2;