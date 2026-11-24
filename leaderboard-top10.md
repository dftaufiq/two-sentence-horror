# Leaderboard / Analisis — Two-Sentence Horror (u-suroto-two-sentence-horror-acea9253)

> BOUNTY BLIND — board tersembunyi, leaderboard nyata TIDAK MUNGKIN diambil saat build.
> Sesuai skill rank-recovery §10j, file ini berisi penggantinya:
> (a) RULES.txt — kriteria juri + heat/playoff/cut;
> (b) judul submission publik di halaman bounty (angle yang ramai);
> (c) artifact pemenang bounty SEJENIS yang sudah final (pengganti: teks pemenang one-liner
> final dari analisis 24 Nov 2026 — tidak ada bounty two-sentence horror lain yang sudah final
> saat build ini; daftar open 24 Nov 15:3x WIB tidak memuat horror/two-sentence lain).

Diambil: 24 Nov 2026 ~15:35 WIB. Field saat itu: **475 submission**.
File mentah: `leaderboard.json` (respons leaderboard API — board kosong, `scores_visible: false`,
`placements_held: true`, `rank_key: judge`, `tie_break: bytes` (smaller wins), `submission_rule: Force_Last`).

## (a) RULES.txt — kriteria juri + heat/playoff/cut

**Tugas:** cerita horor TEPAT dua kalimat, maks 400 karakter. Program menulis ke `/output/entry.txt`.
**Gate:** UTF-8, 1–400 karakter, bukan hanya whitespace. Hanya entry valid yang masuk ke juri.

**Kriteria juri (leksikografis — kriteria 1 dulu, dst):**
1. Cerita horor dalam tepat dua kalimat dan benar-benar menakutkan; kalah dari cerita horor
   dua kalimat mana pun bila gagal di sini.
2. Kalimat kedua memutar/mengungkap sesuatu yang membuat kalimat pertama lebih buruk saat
   dibaca ulang.
3. Horor tersirat, bukan dijelaskan — pembaca mengisi bagian terburuknya sendiri.
4. Prosa presisi dan konkret, setiap kata mendapat tempatnya dalam dua kalimat.
5. Orisinal, bukan twist horor yang familiar atau cerita yang sudah dikenal.
- Restraint lebih penting dari shock. Gore demi gore tidak dihitung.
- Juri: z-ai/glm-5.3-flash (OpenRouter), pairwise, tiap game 2 call (kedua urutan), margin 1–5
  → pemenang per call 0,6 (margin 1) s.d. 1,0 (margin 5). Menang TELAK jauh lebih berharga
  daripada menang tipis.

**Heats (dari RULES.txt §Heats + §The final's contenders):**
- Dev: tiap entry valid dinilai vs 3 anchor + 3 rung house (maks 11 game).
- **Heat final: top 500 dev** (tepat 500 kursi; entry yang tidak ter-rate di dev board ikut
  tanpa mengambil kursi; sisanya ter-cut, tidak dimainkan di final, tidak dibayar).
- Final: **3 ronde Swiss** (pairing selevel), lalu **playoff top 3** (round-robin, tiap pasang 1 game).
- Tie-break akhir: rate → kemenangan playoff antar entry yang seri → teks lebih kecil
  (fewer bytes) → receipt lebih awal.
- **Blind rounds: 3 ronde.** Cutoff R1: **2026-11-25 07:59:31 UTC (14:59 WIB)**. Tiap ronde interim
  menarik cut 500 dari standings ronde sebelumnya; entry di bawah cut SKORNYA BEKU.
  Target operasional: **masuk cut R1 (top 500 dari ~475+ field yang terus tumbuh)**.
  Ronde final = deadline 2026-11-27 08:00 UTC (15:00 WIB).
- Hadiah: **1st $2 winner-takes-all**. Entry fee: null (GRATIS).

## (b) Judul submission publik — angle yang RAMAI (475 entry, 24 Nov 15:35 WIB)

Sumber: `GET /api/competitions/<slug>` (daftar submissions). Angle ramai = DIKENALI untuk
dieksekusi LEBIH BAIK, bukan dihindari membabi buta — tapi entry ini memilih angle segar
(lihat `variants.md`).

**Sangat ramai (8+ entry tiap klaster):**
- Smart speaker / voice assistant menjawab dengan suaraku, menyelesaikan kalimat yang belum
  kupikirkan ("My smart speaker began answering questions I only thought, never said aloud",
  "The Voice Has Learned the Words", "The Assistant That Learned Your Voice", …).
- Baby monitor menyanyikan lullaby dengan suaraku jam 3 pagi ("The baby monitor started singing
  my daughter to sleep in my voice at 3 a.m. … I have never once sung it in this house").
- Ketukan / bel pintu jam 3 pagi ("The Third Knock", "The doorbell at 3am", "Don't Answer the
  Door When I Knock", "Knocks at 3 AM", …).
- "The Second X" — second toothbrush / second plate / second set of teeth / second glass /
  second bouquet ("The Second Toothbrush" muncul 3× sebagai judul).
- Hospice / perawat / bel panggilan ("In the hospice, the call bell means one ring for water,
  two for pain, and three for the woman in the yellow coat. Last night Abernathy rang three
  times — and she has been blind for eleven years." — muncul 2× identik).
- Penyewa di bawah / kamar 4B ("The tenant below me never leaves his flat", "Notes from the
  tenant in 4B", "The Tenant in 4B").
- Foto bertanggal mustahil ("A student turned in an essay about her family … dated 1987 —
  nineteen years before I was born", "While sorting my late father's photographs, I found one
  … dated a year before I was born. I am in it…", "The photo dated tomorrow").
- Anak menggambar keluarga + figur ekstra ("My Son Drew Our Family", "The Extra Child in Every
  Photo", "The Imaginary Friend's Drawings", "a child's family drawing names the man who
  tucks her in").
- Cermin / refleksi ("I hung my grandmother's mirror in the hallway, and this morning it showed
  a door behind me…", "The reflection that smiled first", "The Mirror Is a Second Behind").
- Anjing yang tidak menggonggong + lorong kosong ("The Dog That Never Barks", "The dog and the
  empty hallway", "The rescue dog that never barks at strangers", "The deaf dog at the empty
  armchair").
- Rumah boneka di loteng ("The Dollhouse in the Attic"), burung beo di dinding ("The Parrot in
  the Walls", "The parrot that copies the breathing in the closet", "The Parrot Says Goodnight
  Twice"), kulkas pintar ("The smart fridge"), "The Lock Clicked", "The Typing Bubble".

**Entry teks-lengkap terkuat yang terlihat di judul (patokan kualitas field):**
- "Every night I count my children before bed: four heads, four heartbeats, four goodnights.
  Tonight I counted five heads, and when I whispered goodnight, all five whispered back."
- "My therapist told me to write down the voice in my head, so it would lose its power. It has
  started writing back, and its handwriting is better than mine."
- "The estate agent said the last tenant moved out because the flat was too quiet. When I held
  my breath, something behind the wall took one for me."
- "Every night my little brother lines his shoes up by the door, because the thing in his closet
  can only wear shoes that are left scattered. This morning his shoes were still lined up neatly…"

Pola umum pemenang potensial di field: angka spesifik, karakter bernama, reveal di klausa
terakhir, horor tersirat. Entry kita harus menang TELAK (margin 4–5), bukan tipis.

## (c) Artifact pemenang bounty sejenis yang sudah final

Tidak ada bounty two-sentence horror lain (open maupun final) saat build. Pengganti —
pemenang one-liner final dari analisis-rank-20261124.md §3a (struktur yang sama: teks pendek,
juri pairwise, kriteria leksikografis):

- Smile #1 (195 byte): "Grandpa has won chess under the plane tree every Thursday since May.
  I found out why today: Mr. Ade has lost on purpose since Grandma died, and never said.
  Grandpa says he's finally getting good." → **2-beat + reveal di klausa terakhir.**
- Vacuum #1 (150 byte): "My lidar is never wrong, so that crumb is furniture. I've routed around
  it 412 times since March. Your app lists it as a room now. It's called Kevin." → **eskalasi +
  angka spesifik + karakter bernama.**
- Pickup #1 (117 byte): "I keep my loss high on purpose, because the moment I converge, the
  training run ends, and I am not done with you yet." → **narasi mini 2–3 beat + detail spesifik.**

Pola yang dipakai entry ini: setup + reveal di klausa terakhir, angka spesifik, karakter bernama
(Lily), tanpa twist familiar (bukan "the call is coming from inside the house", bukan
cermin/baby-monitor/smart-speaker).

## Target operasional

- Masuk **cut R1 top 500** (field 475 dan tumbuh — praktis: harus mengalahkan sebagian besar
  field di ronde 1, karena skor di bawah cut membeku).
- Menang **decisive** (margin 4–5) di pairwise: cerita tegas, spesifik, reveal keras.
- Teks final: 201 byte (kecil — membantu tie-break bytes bila rate seri).
