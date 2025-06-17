import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "roblox") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001741133131"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001841428029")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1001780451521"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "732448606"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "10"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#111 #112 #random #menfess #jj #collab").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
hi, join dulu ke channel yang ada dibawah untuk bisa kirim pesan ke channel @robloxbaseid
""")
start_msg = os.getenv("START_MSG", """
halo {mention}
pesan, pap dan video yang kalian kirim di @robloxautobot akan otomatis di post ke @robloxbaseid

❌ Spam
❌ Porn
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅 periksa hastag atau ketik /help.

gc roblox keren @robloxgrupindonesia
""")
