import requests 
from datetime import datetime

def get_day_of_week(date_string: str) -> str:
    """根据日期字符串返回对应的星期几名称"""
    date_object = datetime.strptime(date_string, "%Y-%m-%d")  # 将字符串转换为日期对象
    # 获取星期几，weekday() 方法返回的值是星期一为 0，星期天为 6
    day_of_week_number = date_object.weekday()
    # 将数字转换为对应的星期几名称
    days_of_week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    day_of_week_name = days_of_week[day_of_week_number]
    return day_of_week_name

class Weather:
    def __init__(self):
        self.key = "aedc97eaa1fd4b148476a0afa47c60ee"  # key

    def get_loc_id(self, city_name: str) -> str:
        """获取城市ID"""
        # 中国城市代码查询
        loc_url = f"https://geoapi.qweather.com/v2/city/lookup?location={city_name}&key={self.key}"

        resp = requests.get(loc_url)
        loc_id = resp.json()['location'][0]['id']
        return loc_id
    
    def get_weather(self, loc_id: str) -> dict:
        """获取当日天气信息"""
        weather_url = f"https://devapi.qweather.com/v7/weather/now?location={loc_id}&key={self.key}"
        resp = requests.get(weather_url)
        data = resp.json()
        temp = data['now']['temp'] + "°C" # 温度
        # temp = "12°C" # 温度
        feels_like = data['now']['feelsLike'] + "°C" # 体感温度
        text = data['now']['text']  # 天气
        wind_dir_scale = data['now']['windDir'] + data['now']['windScale'] + "级" # 风向风力
        wind_speed = data['now']['windSpeed'] + "km/h" # 风速
        humidity = data['now']['humidity'] + "%"# 湿度
        precip = data['now']['precip'] + "mm" # 降水量
        vis = data['now']['vis'] + "km" # 能见度
        cloud = data['now']['cloud'] + "%"# 云量
        return temp,feels_like,text, wind_dir_scale, wind_speed,humidity,precip,vis,cloud
    
    def get_weather_7d(self, loc_id: str) -> list:
        """获取7天天气预报"""
        weather_url = f"https://devapi.qweather.com/v7/weather/7d?location={loc_id}&key={self.key}"
        resp = requests.get(weather_url)
        data = resp.json()
        daily_data = data['daily']
        weather_7d = []
        for day in daily_data:
            date = day['fxDate']  # 
            text_day = day['textDay']  # 白天天气现象
            text_night = day['textNight']  # 夜间天气现象
            temp_min = day['tempMin']  # 最低温度
            temp_max = day['tempMax']  # 最高温度
            weather_7d.append({
                "week": get_day_of_week(date_string=date),# 星期几
                "weather": text_day if text_day==text_night else f"{text_day}转{text_night}",
                "temp": f"{temp_min}°C-{temp_max}°C",
            })
        weather_sun = {
            "sunrise": daily_data[0]['sunrise'],  # 日出时间
            "sunset": daily_data[0]['sunset'],    # 日落时间
            }
        weather_day = {
            "temp_min": daily_data[0]['tempMin'] + "°C",  # 最低温度
            "temp_max": daily_data[0]['tempMax'] + "°C" # 最高温度
        }
        return weather_7d, weather_sun, weather_day
    
    def get_weather_24h(self, loc_id: str) -> list:
        """获取24小时天气预报"""
        weather_url = f"https://devapi.qweather.com/v7/weather/24h?location={loc_id}&key={self.key}"
        resp = requests.get(weather_url)
        data = resp.json()
        hourly_data = data['hourly']
        weather_24h = []
        for hour in hourly_data:
            time = hour['fxTime']  # 预报时间
            text = hour['text']  # 天气现象
            temp = hour['temp']  # 温度
            weather_24h.append({
                "time": time.split("T")[1].split("+")[0],  # 只保留时间部分
                "weather": text,
                "temp": f"{temp}°C",
            })
        return weather_24h
    


if __name__ == "__main__":
    weather = Weather()
    loc_id = weather.get_loc_id("邳州")
    resp = weather.get_weather_7d(loc_id)
    print(resp)