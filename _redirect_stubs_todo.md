# 重定向存根待删登记（TOOLBOX-REDIRECT Stubs → 保留 1 个月后删除）

> 本文件是 `AGENTS.md` §4.6 规定的**统一登记处**。所有 `TOOLBOX-REDIRECT` 迁移存根（临时过渡，最长保留 **1 个月**）必须登记于此，到期由维护者**主动删除**，**不依赖定时任务**。
>
> 维护约定：
> - 新建重定向存根的同一批次 → 在此追加一行 + 同步 `--no-verify` 提死链（见 §4.6）。
> - 到「到期日」后 → 按底部「删除 SOP」主动处理，并把状态改为「已删（commit xxx）」。
> - 每条记录删完后**保留历史行**（标「已删」），便于审计，不要整行删除。

## 字段
| 字段 | 含义 |
|------|------|
| 源 URL | 旧地址（重定向存根，到期真正 404） |
| 目标 URL | 新地址（跳转目的地） |
| 建存根日期 | 写入 `TOOLBOX-REDIRECT` 的日期 |
| 到期日 | 建存根日期 + 1 个月，须物理删除 |
| 状态 | 待删 / 已删（注明删除 commit） |
| 备注 | 繁体 zh-tw 由 CI 自动消失等 |

## 待删清单

| 源 URL | 目标 URL | 建存根日期 | 到期日 | 状态 | 备注 |
|--------|----------|-----------|--------|------|------|
| https://tools.dicomp.net/tools/pets/pet-age-convert.html | https://tools.dicomp.net/tools/pet/pet-age-converter.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 繁体 `zh-tw/tools/pets/pet-age-convert.html` 同规则，CI 自动消失 |
| https://tools.dicomp.net/tools/pets/feeding-amount.html | https://tools.dicomp.net/tools/pet/pet-feeding-calc.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 繁体同理 |
| https://tools.dicomp.net/tools/pets/vaccine-reminder.html | https://tools.dicomp.net/tools/pet/reminder-vaccine-deworming.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 繁体同理 |
| https://tools.dicomp.net/tools/pets/grooming-guide.html | https://tools.dicomp.net/tools/pet/grooming-guide.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 繁体同理 |
| https://tools.dicomp.net/tools/pets/kennel-space.html | https://tools.dicomp.net/tools/pet/kennel-space.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 繁体同理 |
| https://tools.dicomp.net/tools/pets/index.html | https://tools.dicomp.net/tools/pet/index.html | 2026-10-10 | 2026-11-10 | 已删（ea0240209b） | 分类落地页存根；繁体同理 |
| https://tools.dicomp.net/tools/music/frequency-3.html | https://tools.dicomp.net/tools/music/instrument-tuning.html | 2026-10-12 | 2026-11-12 | 已删（本批次，含死链补录） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/insurance/calc-pv-1.html | https://tools.dicomp.net/tools/realestate/pv.html | 2026-08-25 | 2026-09-25 | 已删（2026-11-03） | 2026-10-25 公式审计时发现漏登记；指南 15 处反链已改指新 URL；繁体由 CI 自动消失 |
| https://tools.dicomp.net/tools/insurance/estimate-20.html | https://tools.dicomp.net/tools/insurance/surrender-value.html | 2026-08-25 | 2026-09-25 | 已删（2026-11-03） | 同上 |
| https://tools.dicomp.net/tools/insurance/stats-5.html | https://tools.dicomp.net/tools/insurance/loss-ratio.html | 2026-08-25 | 2026-09-25 | 已删（2026-11-03） | 同上 |
| https://tools.dicomp.net/tools/general/calculator-calc-11.html | https://tools.dicomp.net/tools/math/complex-number.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc/unit-prefix.html | https://tools.dicomp.net/tools/general/convert-22.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc/scientific-notation.html | https://tools.dicomp.net/tools/general/convert-21.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc/statistics-distribution.html | https://tools.dicomp.net/tools/general/calc-stats-1.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc/truth-table.html | https://tools.dicomp.net/tools/general/generator-23.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc2/tax-refund.html | https://tools.dicomp.net/tools/travel/estimate-15.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc2/cigarette-tar.html | https://tools.dicomp.net/tools/health/convert-content.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/misc2/coin-grade.html | https://tools.dicomp.net/tools/antiques/rater-1.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/niche/succulent-watering.html | https://tools.dicomp.net/tools/gardening/reminder-cycle-succulent.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/niche/convert-fps.html | https://tools.dicomp.net/tools/video/video-fps.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/niche/convert-sample.html | https://tools.dicomp.net/tools/audio/audio-sample-rate.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/niche/recommender-temp-pottery.html | https://tools.dicomp.net/tools/ceramics/ceramic-firing.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |
| https://tools.dicomp.net/tools/niche/photography-exposure.html | https://tools.dicomp.net/tools/photo/calc-exposure-aperture.html | 2026-10-12 | 2026-11-12 | 已删（839719048a） | 跨分类重复副本；繁体同理 |

| https://tools.dicomp.net/tools/agriculture/estimate-analysis.html | https://tools.dicomp.net/tools/agriculture/canopy-coverage.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/edu/stats.html | https://tools.dicomp.net/tools/edu/essay-word-counter.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/edu/ranking.html | https://tools.dicomp.net/tools/edu2/exam-analysis.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/edu/wenbenquzhong-paixu-fanzhuan.html | https://tools.dicomp.net/tools/it/text-dedupe-sort.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/cardiology/convert-rehab.html | https://tools.dicomp.net/tools/cardiology/cardiac-rehab-mets.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/design/analysis.html | https://tools.dicomp.net/tools/design/palette-extractor.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/design/generator-time-1.html | https://tools.dicomp.net/tools/video/subtitle-tool.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/design/color-contrast-check.html | https://tools.dicomp.net/tools/design/contrast-checker.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/electrical/voltage-capacity-battery.html | https://tools.dicomp.net/tools/electrical/battery-bank.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/electrical/calc-power-capacitance.html | https://tools.dicomp.net/tools/electrical/power-factor-compensation.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/rehabilitation/analysis-time.html | https://tools.dicomp.net/tools/rehabilitation/gait-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/usedcar/estimate-14.html | https://tools.dicomp.net/tools/usedcar/car-residual.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/pulmonology/analysis-14.html | https://tools.dicomp.net/tools/pulmonology/tb-resistance.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/acupuncture/analysis-10.html | https://tools.dicomp.net/tools/acupuncture/cupping-mark-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/property/area-shared.html | https://tools.dicomp.net/tools/property/shared-area.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/metallurgy/estimate-temp-time-1.html | https://tools.dicomp.net/tools/metallurgy/decarburization.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/forensic-medicine/analysis-15.html | https://tools.dicomp.net/tools/forensic-medicine/fall-injury.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/it/analysis-66.html | https://tools.dicomp.net/tools/science/statistics-calculator.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/it/analysis-manager-1.html | https://tools.dicomp.net/tools/science/statistics-calculator.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/science/yiyuanercifangchengqiujie.html | https://tools.dicomp.net/tools/math/quadratic-solver.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/railway/noise-1.html | https://tools.dicomp.net/tools/eco/noise-superposition.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/railway/qiaoliang-qiaodun-zhizuo-hezai.html | https://tools.dicomp.net/tools/bridge/load-calc.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/railway/slope-4.html | https://tools.dicomp.net/tools/road/grade-calc.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/analysis-4.html | https://tools.dicomp.net/tools/fun/blood-type-personality.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/laugh-generator.html | https://tools.dicomp.net/tools/fun/generator-laugh.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/convert-speed-stride.html | https://tools.dicomp.net/tools/fitness/step-stride.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/caishuzi-1-100fanwei.html | https://tools.dicomp.net/tools/fun/number-guess.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/sudoku-generator.html | https://tools.dicomp.net/tools/fun/generator-2.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/maze-generator.html | https://tools.dicomp.net/tools/fun/generator-3.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/analysis-tester-rhythm.html | https://tools.dicomp.net/tools/fun/typing-rhythm.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fun/stats-blink.html | https://tools.dicomp.net/tools/fun/blink-counter.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/food-testing/summary.html | https://tools.dicomp.net/tools/food-testing/heavy-metal-migration.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/library/convert-ref-cite.html | https://tools.dicomp.net/tools/library/citation-format.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/language/hanyuyanwenchaijie-yuanyin-fuyin.html | https://tools.dicomp.net/tools/language/korean-hangul-decomposer.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/language/xibanyayuzhongyinweizhipanduan-neizhiguize.html | https://tools.dicomp.net/tools/language/spanish-accent-rules.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/obstetrics/gonggao-fuweiyutaiertizhong-hadlock.html | https://tools.dicomp.net/tools/obstetrics/fetal-weight-hadlock.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/baking/mold.html | https://tools.dicomp.net/tools/baking/mold-volume.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/sports/tent-wind-rating.html | https://tools.dicomp.net/tools/travel/zhangpengfangfengxishu.html | 2026-10-12 | 2026-11-12 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/sports/convert-13.html | https://tools.dicomp.net/tools/sports/climbing-grade-converter.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/safety/stats-report-frequency.html | https://tools.dicomp.net/tools/safety/accident-stats.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/optical/mobian-jianbian-pingbian-guige.html | https://tools.dicomp.net/tools/optical/edge-bevel.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/pet/kouling-shoushichongfucishuyujiyiquxian.html | https://tools.dicomp.net/tools/pet-training/command-repetition.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/clinical-lab/analysis-8.html | https://tools.dicomp.net/tools/clinical-lab/blood-gas-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/clinical-lab/analysis-9.html | https://tools.dicomp.net/tools/clinical-lab/electrophoresis-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/clinical-lab/analysis-density-2.html | https://tools.dicomp.net/tools/clinical-lab/semen-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/hr/analysis-conversion-recruit.html | https://tools.dicomp.net/tools/hr/recruitment-funnel.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/hr/stats-report-attendance.html | https://tools.dicomp.net/tools/hr/attendance-stats.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/food-processing/estimate-analysis-1.html | https://tools.dicomp.net/tools/food-processing/residual-oxygen.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/marketing/analysis-strength-market-share.html | https://tools.dicomp.net/tools/marketing/market-share.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fitness/estimate-1.html | https://tools.dicomp.net/tools/fitness/calc-4.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/fitness/carbon-ratio.html | https://tools.dicomp.net/tools/fitness/macro-ratio.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/tcm-pharmacy/analysis-ratio-prescription.html | https://tools.dicomp.net/tools/tcm-pharmacy/jun-chen-zuo-shi.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/ophthalmology/analysis-12.html | https://tools.dicomp.net/tools/ophthalmology/visual-field-analysis.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/metalwork/voltage-current.html | https://tools.dicomp.net/tools/welding/speed-voltage-current.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/metalwork/banjin-jianzhe-chongya-maohan-gongyi.html | https://tools.dicomp.net/tools/metalwork/sheet-bend.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/metalwork/qiege-denglizi-huoyan-shuidao-canshu.html | https://tools.dicomp.net/tools/electrical/speed-9.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/legal/falvwenshuguanjiancizidongtiqu.html | https://tools.dicomp.net/tools/legal2/keyword-extract.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/legal/estimate-12.html | https://tools.dicomp.net/tools/legal/labor-compensation.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/legal/falv-yijian-han-beiwanglu-bianxie.html | https://tools.dicomp.net/tools/legal/generator-17.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/legal/estimate-40.html | https://tools.dicomp.net/tools/legal/work-injury-compensation.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/dentistry/length-3.html | https://tools.dicomp.net/tools/dentistry/dental-arch-development.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/dentistry/analysis-11.html | https://tools.dicomp.net/tools/dentistry/bridge-span.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/dentistry/kouqiangai-tnm-shaichagongju.html | https://tools.dicomp.net/tools/dentistry/oral-cancer-screening.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/reproductive-medicine/stats-6.html | https://tools.dicomp.net/tools/reproductive-medicine/ivf-statistics.html | 2026-09-19 | 2026-10-19 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/photo/capacity-fps.html | https://tools.dicomp.net/tools/photo2/video-storage.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/surveying/distance-4.html | https://tools.dicomp.net/tools/surveying/horizontal-from-slope.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/hematology/quetie-juyou-rongxue-shiyanshijianbie.html | https://tools.dicomp.net/tools/hematology/anemia-differential.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/machinery/speed-cutting-feed.html | https://tools.dicomp.net/tools/mechanical/cutting-speed.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |
| https://tools.dicomp.net/tools/machinery/zaoyin-shengya-pinpu-jiangzao-yugu.html | https://tools.dicomp.net/tools/eco/noise-addition.html | 2026-09-22 | 2026-10-22 | 已删（本批次） | 2026-11-03 审计补登记；繁体同理 |

## 删除 SOP（到期执行）
1. `cd /Users/cgw/project/cgw/chenguangwu.github.io`
2. 先 grep 全站（排除 `zh-tw/`、排除 `tools/pets/` 存根自身）所有指向待删源 URL 的内部链接（`href`/`src`），改写为目标 URL 或删除，避免删除后产生内部死链（`_audit_links.py` 门禁不过）。
3. `git rm tools/pets/<file>.html …`（删空目录由 git 处理）。
4. `zh-tw/` 是 CI 构建产物，删源后自动消失，无需手动删。
5. `python3 scripts/run_gates.py` → 确认 216 项全过（存根本就被 `_test_static` 跳过，删除不应破坏门禁）。
6. 旧 URL 已是真 404，用默认校验提死链：`python3 _submit_indexnow_deadlinks.py --file _deadlinks_2026-10-10_pets.txt`（脚本自动 HTTP 校验，只交已 404 的；**不要再 `--no-verify`**）。
7. `git add -A` → `commit`（说明「删除 pets 重定向存根，旧 URL 真正 404」）→ `push origin master`。
8. 单次查询 GitHub Actions 确认部署成功（不轮询）。
9. 回本文件把对应行状态改为「已删（commit xxx）」。

## 2026-11-16 校正：存量 29 个存根按真实建存根日期登记（均在保留期内）

> 来源：全站 `grep TOOLBOX-REDIRECT`（29 文件）。建存根日期取每个文件首次引入 `TOOLBOX-REDIRECT` 的提交作者日期，
> 逐文件执行 `git log --reverse --format='%ad %h' --date=short -S TOOLBOX-REDIRECT -- <文件>`，
> 29 个文件均为 2026-11-14（提交 `029cf0e035` 5 个、`d58e5d690f` 11 个、`760de4410b` 6 个、`34ec610b81` 6 个、`13bb26182e` 1 个），
> 非原页面入库日 2026-08-25。到期日按 +1 个月记 2026-12-14，当前状态「保留期内」。
> 到期后删除须按「删除 SOP」：全站内链改写 → 删文件 → `sitemap-deadlinks.xml` 登记 → 部署 success 后 `_submit_indexnow_deadlinks.py`。

| 源 URL | 目标 URL | 建存根日期 | 到期日 | 状态 | 备注 |
|---|---|---|---|---|---|
| https://tools.dicomp.net/tools/acoustics/intensity-level.html | https://tools.dicomp.net/tools/acoustics/sound-intensity-level.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/agriculture/calc-2.html | https://tools.dicomp.net/tools/agriculture/calculator-calc-density.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/biz/text-compare.html | https://tools.dicomp.net/tools/it/text-diff.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/generator-9.html | https://tools.dicomp.net/tools/biz/barcode-generator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/image-cropper.html | https://tools.dicomp.net/tools/image/image-crop.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/image-resizer.html | https://tools.dicomp.net/tools/image/image-resize.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dynamics/inelastic-collision.html | https://tools.dicomp.net/tools/dynamics/momentum-conservation.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dynamics/period-pendulum.html | https://tools.dicomp.net/tools/science/pendulum-period.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/economics/pv-annuity.html | https://tools.dicomp.net/tools/insurance/annuity-present.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/edu/generator-4.html | https://tools.dicomp.net/tools/it/summary-generator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/energy/electrical-power.html | https://tools.dicomp.net/tools/electromagnetism/electric-power.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/password.html | https://tools.dicomp.net/tools/it/password-generator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/word-counter.html | https://tools.dicomp.net/tools/text/stats-1.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/fitness/calculator-calc-constitution.html | https://tools.dicomp.net/tools/healthcare/bmi-calculator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hr/overtime-pay-calc.html | https://tools.dicomp.net/tools/legal/overtime-pay.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/investment/annuity-pv-inv.html | https://tools.dicomp.net/tools/insurance/annuity-present.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/it/calc-2.html | https://tools.dicomp.net/tools/life/base-convert.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/math/calc-1.html | https://tools.dicomp.net/tools/life/percentage-calculator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/mechanical/calc-1.html | https://tools.dicomp.net/tools/machinery/calc-lifespan-belt.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/medical/calculator-calc-due-date.html | https://tools.dicomp.net/tools/health/pregnancy-due-date.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/nuclear/specific-activity-from-halflife.html | https://tools.dicomp.net/tools/nuclear/specific-activity.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/optical/rayleigh-resolution.html | https://tools.dicomp.net/tools/optics/rayleigh-criterion.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/optical/snell-refraction.html | https://tools.dicomp.net/tools/glass/snell-refraction.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/pet/pet-age-converter.html | https://tools.dicomp.net/tools/pet/pet-age.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/realestate/calc-2.html | https://tools.dicomp.net/tools/finance/rental-yield-calculator.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/safety/detector-strength.html | https://tools.dicomp.net/tools/it/password-strength.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/science/factorial-calculator.html | https://tools.dicomp.net/tools/math/factorial-calc.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/science/range-calculator.html | https://tools.dicomp.net/tools/statistics/range-stat.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/statistics/variance-list.html | https://tools.dicomp.net/tools/statistics/sample-variance.html | 2026-11-14 | 2026-12-14 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/cosmetic-derm/time-23.html | https://tools.dicomp.net/tools/cosmetic-derm/post-procedure-recovery.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/cosmetic-derm/area-12.html | https://tools.dicomp.net/tools/cosmetic-derm/telangiectasia-area.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/cosmetic-derm/pifuphceding.html | https://tools.dicomp.net/tools/cosmetic-derm/skin-ph.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/life/date-diff.html | https://tools.dicomp.net/tools/life/date-difference-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/sports/youyonghuashuixiaolv-swolf.html | https://tools.dicomp.net/tools/sports/swimming-stroke-efficiency.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/psychiatry/lsas-social.html | https://tools.dicomp.net/tools/psychiatry/rater-23.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/clinical-nursing/braden-score.html | https://tools.dicomp.net/tools/clinical-nursing/calc-rater-risk.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/calc-2.html | https://tools.dicomp.net/tools/finance/irr-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dentistry/rater-risk-2.html | https://tools.dicomp.net/tools/dentistry/caries-risk.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hematology/pnh-flow.html | https://tools.dicomp.net/tools/hematology/detector-5.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/calc-3.html | https://tools.dicomp.net/tools/finance/npv-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/clinical-nursing/morse-score.html | https://tools.dicomp.net/tools/clinical-nursing/assessor-rater-risk.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/clinical-nursing/generator-pressure.html | https://tools.dicomp.net/tools/clinical-nursing/pressure-injury-description.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hematology/generator-analysis.html | https://tools.dicomp.net/tools/hematology/thrombin-generation.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/food-testing/generator-27.html | https://tools.dicomp.net/tools/food-testing/colony-count.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/obstetrics/calc-risk.html | https://tools.dicomp.net/tools/obstetrics/down-screening.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dentistry/assessor-5.html | https://tools.dicomp.net/tools/dentistry/zirconia-aesthetics.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/clinical-nursing/surgical-position-risk.html | https://tools.dicomp.net/tools/clinical-nursing/assessor-pressure-risk.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hematology/mpn-scoring.html | https://tools.dicomp.net/tools/hematology/rater-5.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/obstetrics/kupperman-score.html | https://tools.dicomp.net/tools/obstetrics/rater-26.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/endocrinology/sex-hormone-cycle.html | https://tools.dicomp.net/tools/endocrinology/cycle-hormone.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hvac/kongtiaolengfuhejisuan.html | https://tools.dicomp.net/tools/hvac/cooling-load.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/pulmonology/calc-48.html | https://tools.dicomp.net/tools/pulmonology/oxygenation-index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/rheumatology/assessor-10.html | https://tools.dicomp.net/tools/rheumatology/essdai.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/rheumatology/rater-16.html | https://tools.dicomp.net/tools/rheumatology/sledai.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/neurology/twstrs.html | https://tools.dicomp.net/tools/neurology/rater-21.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/psychiatry/cdrisc-resilience.html | https://tools.dicomp.net/tools/psychiatry/rater-24.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/psychiatry/asrs-adhd.html | https://tools.dicomp.net/tools/psychiatry/self-assess-4.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/pulmonology/feigongneng-fev1-fvc-fenji.html | https://tools.dicomp.net/tools/pulmonology/pulmonary-function.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/obstetrics/placenta-grading.html | https://tools.dicomp.net/tools/obstetrics/taipanchengshudu-grannumfenji.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/ophthalmology/osdi-scale.html | https://tools.dicomp.net/tools/ophthalmology/self-assess-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/rehabilitation/berg-balance-scale.html | https://tools.dicomp.net/tools/rehabilitation/tester-rater.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/gastroenterology/hp-resistance.html | https://tools.dicomp.net/tools/gastroenterology/detector-7.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/urology/iief5-score.html | https://tools.dicomp.net/tools/urology/rater-4.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/neurology/rater-19.html | https://tools.dicomp.net/tools/neurology/updrs.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/nephrology/aki-kdigo.html | https://tools.dicomp.net/tools/nephrology/jixingshensunshang-kdigo-fenqi.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/salary-after-tax.html | https://tools.dicomp.net/tools/finance/salary-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/fishery/feed-rate-calculator.html | https://tools.dicomp.net/tools/fishery/feeding-rate.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/eco/noise-addition.html | https://tools.dicomp.net/tools/eco/noise-superposition.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/shadow-generator.html | https://tools.dicomp.net/tools/design/css-box-shadow-generator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/it/html-entity-encoder.html | https://tools.dicomp.net/tools/it/html-entities-encode.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/it/whitespace.html | https://tools.dicomp.net/tools/it/text-cleaner.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/it/calc-3.html | https://tools.dicomp.net/tools/it/color-converter.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/ai/token.html | https://tools.dicomp.net/tools/ai/token-usage.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/acoustics/spl-add.html | https://tools.dicomp.net/tools/acoustics/combine-two-spl.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/acoustics/decibel-power.html | https://tools.dicomp.net/tools/acoustics/decibel-power-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/acoustics/decibel-voltage.html | https://tools.dicomp.net/tools/acoustics/decibel-voltage-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/guides/generator-4-guide.html | https://tools.dicomp.net/tools/it/summary-generator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至摘要生成器工具页 |
| https://tools.dicomp.net/guides/variance-list-guide.html | https://tools.dicomp.net/guides/sample-variance-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至sample-variance 使用指南 |
| https://tools.dicomp.net/guides/period-pendulum-guide.html | https://tools.dicomp.net/guides/pendulum-period-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至pendulum-period 使用指南 |
| https://tools.dicomp.net/guides/annuity-pv-inv-guide.html | https://tools.dicomp.net/guides/annuity-present-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至annuity-present 使用指南 |
| https://tools.dicomp.net/guides/twstrs-guide.html | https://tools.dicomp.net/guides/rater-21-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至rater-21 使用指南 |
| https://tools.dicomp.net/guides/rater-19-guide.html | https://tools.dicomp.net/guides/updrs-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至updrs 使用指南 |
| https://tools.dicomp.net/guides/sex-hormone-cycle-guide.html | https://tools.dicomp.net/guides/cycle-hormone-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至cycle-hormone 使用指南 |
| https://tools.dicomp.net/guides/feigongneng-fev1-fvc-fenji-guide.html | https://tools.dicomp.net/guides/pulmonary-function-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至pulmonary-function 使用指南 |
| https://tools.dicomp.net/guides/calc-48-guide.html | https://tools.dicomp.net/guides/oxygenation-index-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至oxygenation-index 使用指南 |
| https://tools.dicomp.net/guides/intensity-level-guide.html | https://tools.dicomp.net/tools/acoustics/sound-intensity-level.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至声强级（L_I = 10·log₁₀(I / I₀)）工具页 |
| https://tools.dicomp.net/guides/decibel-voltage-guide.html | https://tools.dicomp.net/tools/acoustics/decibel-voltage-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至电压分贝（L = 20·log₁₀(V / V₀)）工具页 |
| https://tools.dicomp.net/guides/decibel-power-guide.html | https://tools.dicomp.net/tools/acoustics/decibel-power-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至功率分贝（L = 10·log₁₀(P / P₀)）工具页 |
| https://tools.dicomp.net/guides/spl-add-guide.html | https://tools.dicomp.net/tools/acoustics/combine-two-spl.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至两声压级叠加（L = 10·log₁₀(10^(L₁/10)+10^(L₂/10))）工具页 |
| https://tools.dicomp.net/guides/factorial-calculator-guide.html | https://tools.dicomp.net/guides/factorial-calc-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至factorial-calc 使用指南 |
| https://tools.dicomp.net/guides/kongtiaolengfuhejisuan-guide.html | https://tools.dicomp.net/guides/cooling-load-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至cooling-load 使用指南 |
| https://tools.dicomp.net/guides/generator-27-guide.html | https://tools.dicomp.net/guides/colony-count-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至colony-count 使用指南 |
| https://tools.dicomp.net/guides/kupperman-score-guide.html | https://tools.dicomp.net/guides/rater-26-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至rater-26 使用指南 |
| https://tools.dicomp.net/guides/placenta-grading-guide.html | https://tools.dicomp.net/guides/taipanchengshudu-grannumfenji-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至taipanchengshudu-grannumfenji 使用指南 |
| https://tools.dicomp.net/guides/calc-risk-guide.html | https://tools.dicomp.net/guides/down-screening-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至down-screening 使用指南 |
| https://tools.dicomp.net/guides/noise-addition-guide.html | https://tools.dicomp.net/guides/noise-superposition-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至noise-superposition 使用指南 |
| https://tools.dicomp.net/guides/detector-strength-guide.html | https://tools.dicomp.net/tools/it/password-strength.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至密码强度检测工具页 |
| https://tools.dicomp.net/guides/pet-age-converter-guide.html | https://tools.dicomp.net/guides/pet-age-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至pet-age 使用指南 |
| https://tools.dicomp.net/guides/token-guide.html | https://tools.dicomp.net/guides/token-usage-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至token-usage 使用指南 |
| https://tools.dicomp.net/guides/calculator-calc-due-date-guide.html | https://tools.dicomp.net/guides/pregnancy-due-date-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至pregnancy-due-date 使用指南 |
| https://tools.dicomp.net/guides/overtime-pay-calc-guide.html | https://tools.dicomp.net/guides/overtime-pay-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至overtime-pay 使用指南 |
| https://tools.dicomp.net/guides/pv-annuity-guide.html | https://tools.dicomp.net/guides/annuity-present-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至annuity-present 使用指南 |
| https://tools.dicomp.net/guides/salary-after-tax-guide.html | https://tools.dicomp.net/tools/finance/salary-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至工资税后计算器工具页 |
| https://tools.dicomp.net/guides/calculator-calc-constitution-guide.html | https://tools.dicomp.net/guides/bmi-calculator-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至bmi-calculator 使用指南 |
| https://tools.dicomp.net/guides/osdi-scale-guide.html | https://tools.dicomp.net/guides/self-assess-2-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至self-assess-2 使用指南 |
| https://tools.dicomp.net/guides/morse-score-guide.html | https://tools.dicomp.net/guides/assessor-rater-risk-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至assessor-rater-risk 使用指南 |
| https://tools.dicomp.net/guides/surgical-position-risk-guide.html | https://tools.dicomp.net/guides/assessor-pressure-risk-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至assessor-pressure-risk 使用指南 |
| https://tools.dicomp.net/guides/braden-score-guide.html | https://tools.dicomp.net/guides/calc-rater-risk-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至calc-rater-risk 使用指南 |
| https://tools.dicomp.net/guides/generator-pressure-guide.html | https://tools.dicomp.net/guides/pressure-injury-description-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至pressure-injury-description 使用指南 |
| https://tools.dicomp.net/guides/assessor-5-guide.html | https://tools.dicomp.net/guides/zirconia-aesthetics-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至zirconia-aesthetics 使用指南 |
| https://tools.dicomp.net/guides/rater-risk-2-guide.html | https://tools.dicomp.net/guides/caries-risk-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至caries-risk 使用指南 |
| https://tools.dicomp.net/guides/pifuphceding-guide.html | https://tools.dicomp.net/tools/cosmetic-derm/skin-ph.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至皮肤pH测定工具页 |
| https://tools.dicomp.net/guides/time-23-guide.html | https://tools.dicomp.net/guides/post-procedure-recovery-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至post-procedure-recovery 使用指南 |
| https://tools.dicomp.net/guides/area-12-guide.html | https://tools.dicomp.net/guides/telangiectasia-area-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至telangiectasia-area 使用指南 |
| https://tools.dicomp.net/guides/mpn-scoring-guide.html | https://tools.dicomp.net/guides/rater-5-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至rater-5 使用指南 |
| https://tools.dicomp.net/guides/pnh-flow-guide.html | https://tools.dicomp.net/guides/detector-5-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至detector-5 使用指南 |
| https://tools.dicomp.net/guides/generator-analysis-guide.html | https://tools.dicomp.net/guides/thrombin-generation-guide.html | 2026-11-21 | 2026-12-21 | 保留期内 | 指南重定向至thrombin-generation 使用指南 |
| https://tools.dicomp.net/guides/math-calc-2-guide.html | https://tools.dicomp.net/tools/math/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/feeding-amount-guide.html | https://tools.dicomp.net/tools/pet/pet-feeding-calc.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/edu-calc-2-guide.html | https://tools.dicomp.net/tools/edu/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/estimate-40-guide.html | https://tools.dicomp.net/tools/legal/work-injury-compensation.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-report-frequency-guide.html | https://tools.dicomp.net/tools/safety/accident-stats.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/legal-calc-8-guide.html | https://tools.dicomp.net/tools/tax/calc-8.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/calorie-calculator-guide.html | https://tools.dicomp.net/tools/food/food-calorie-counter.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/ophthalmology-calc-1-guide.html | https://tools.dicomp.net/tools/ophthalmology/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/geology-calc-1-guide.html | https://tools.dicomp.net/tools/geology/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/carbon-ratio-guide.html | https://tools.dicomp.net/tools/fitness/macro-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-10-guide.html | https://tools.dicomp.net/tools/acupuncture/cupping-mark-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/insurance-calc-1-guide.html | https://tools.dicomp.net/tools/insurance/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/fitness-calc-5-guide.html | https://tools.dicomp.net/tools/fitness/calc-5.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/speed-cutting-feed-guide.html | https://tools.dicomp.net/tools/mechanical/cutting-speed.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/cardiology-calc-3-guide.html | https://tools.dicomp.net/tools/cardiology/calc-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-15-guide.html | https://tools.dicomp.net/tools/forensic-medicine/fall-injury.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/area-shared-guide.html | https://tools.dicomp.net/tools/property/shared-area.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-5-guide.html | https://tools.dicomp.net/tools/insurance/loss-ratio.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/kouling-shoushichongfucishuyujiyiquxian-guide.html | https://tools.dicomp.net/tools/pet-training/command-repetition.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/base64-guide.html | https://tools.dicomp.net/tools/it/base64-converter.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/surveying-calc-1-guide.html | https://tools.dicomp.net/tools/surveying/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/voltage-current-guide.html | https://tools.dicomp.net/tools/welding/speed-voltage-current.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/convert-rehab-guide.html | https://tools.dicomp.net/tools/cardiology/cardiac-rehab-mets.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/color-blindness-sim-guide.html | https://tools.dicomp.net/tools/design/colorblind-simulator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-8-guide.html | https://tools.dicomp.net/tools/clinical-lab/blood-gas-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/health-calc-1-guide.html | https://tools.dicomp.net/tools/health/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/hematology-calc-1-guide.html | https://tools.dicomp.net/tools/hematology/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/qiege-denglizi-huoyan-shuidao-canshu-guide.html | https://tools.dicomp.net/tools/electrical/speed-9.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/dentistry-calc-1-guide.html | https://tools.dicomp.net/tools/dentistry/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/gradient-generator-guide.html | https://tools.dicomp.net/tools/design/gradient.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/marketing-calc-1-guide.html | https://tools.dicomp.net/tools/marketing/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/quetie-juyou-rongxue-shiyanshijianbie-guide.html | https://tools.dicomp.net/tools/hematology/anemia-differential.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/estimate-analysis-1-guide.html | https://tools.dicomp.net/tools/food-processing/residual-oxygen.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-12-guide.html | https://tools.dicomp.net/tools/ophthalmology/visual-field-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/pet-age-convert-guide.html | https://tools.dicomp.net/tools/pet/pet-age.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/estimate-20-guide.html | https://tools.dicomp.net/tools/insurance/surrender-value.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/accounting-calc-2-guide.html | https://tools.dicomp.net/tools/accounting/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/fitness-calc-2-guide.html | https://tools.dicomp.net/tools/fitness/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/it-bayes-theorem-guide.html | https://tools.dicomp.net/tools/it/bayes-theorem.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/photography-exposure-guide.html | https://tools.dicomp.net/tools/photo/calc-exposure-aperture.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-strength-market-share-guide.html | https://tools.dicomp.net/tools/marketing/market-share.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/color-contrast-check-guide.html | https://tools.dicomp.net/tools/design/contrast-checker.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/it-margin-of-error-guide.html | https://tools.dicomp.net/tools/it/margin-of-error.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/encode-calc-1-guide.html | https://tools.dicomp.net/tools/encode/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/neurology-calc-1-guide.html | https://tools.dicomp.net/tools/neurology/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/maze-generator-guide.html | https://tools.dicomp.net/tools/fun/generator-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/cardiology-calc-1-guide.html | https://tools.dicomp.net/tools/cardiology/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/feed-rate-calculator-guide.html | https://tools.dicomp.net/tools/fishery/feeding-rate.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/estimate-12-guide.html | https://tools.dicomp.net/tools/legal/labor-compensation.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/realestate-calc-2-guide.html | https://tools.dicomp.net/tools/finance/rental-yield-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/health-calc-3-guide.html | https://tools.dicomp.net/tools/health/calc-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/html-entity-encoder-guide.html | https://tools.dicomp.net/guides/cluster-encode.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/capacity-fps-guide.html | https://tools.dicomp.net/tools/photo2/video-storage.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-report-attendance-guide.html | https://tools.dicomp.net/tools/hr/attendance-stats.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/gonggao-fuweiyutaiertizhong-hadlock-guide.html | https://tools.dicomp.net/tools/obstetrics/fetal-weight-hadlock.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/construction-calc-5-guide.html | https://tools.dicomp.net/tools/construction/calc-5.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/it-confidence-interval-guide.html | https://tools.dicomp.net/tools/it/confidence-interval.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/kouqiangai-tnm-shaichagongju-guide.html | https://tools.dicomp.net/tools/dentistry/oral-cancer-screening.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/zaoyin-shengya-pinpu-jiangzao-yugu-guide.html | https://tools.dicomp.net/tools/eco/noise-superposition.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/encode-calc-2-guide.html | https://tools.dicomp.net/tools/encode/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/fitness-calc-4-guide.html | https://tools.dicomp.net/tools/fitness/calc-4.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-4-guide.html | https://tools.dicomp.net/tools/fun/blood-type-personality.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/rayleigh-resolution-guide.html | https://tools.dicomp.net/tools/optics/rayleigh-criterion.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/calc-pv-1-guide.html | https://tools.dicomp.net/tools/realestate/pv.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/recommender-temp-pottery-guide.html | https://tools.dicomp.net/tools/ceramics/ceramic-firing.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-tester-rhythm-guide.html | https://tools.dicomp.net/tools/fun/typing-rhythm.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-14-guide.html | https://tools.dicomp.net/tools/pulmonology/tb-resistance.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/specific-activity-from-halflife-guide.html | https://tools.dicomp.net/tools/nuclear/specific-activity.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/falvwenshuguanjiancizidongtiqu-guide.html | https://tools.dicomp.net/tools/legal2/keyword-extract.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/realestate-calc-1-guide.html | https://tools.dicomp.net/tools/realestate/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-9-guide.html | https://tools.dicomp.net/tools/clinical-lab/electrophoresis-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-density-2-guide.html | https://tools.dicomp.net/tools/clinical-lab/semen-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/math-calc-3-guide.html | https://tools.dicomp.net/tools/math/calc-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/estimate-analysis-guide.html | https://tools.dicomp.net/tools/agriculture/canopy-coverage.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/falv-yijian-han-beiwanglu-bianxie-guide.html | https://tools.dicomp.net/tools/legal/generator-17.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/length-3-guide.html | https://tools.dicomp.net/tools/dentistry/dental-arch-development.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/edu-calc-3-guide.html | https://tools.dicomp.net/tools/edu/calc-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/inelastic-collision-guide.html | https://tools.dicomp.net/tools/dynamics/momentum-conservation.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/banjin-jianzhe-chongya-maohan-gongyi-guide.html | https://tools.dicomp.net/tools/metalwork/sheet-bend.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/marketing-marketing-ltv-calculator-guide.html | https://tools.dicomp.net/tools/marketing/marketing-ltv-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/mobian-jianbian-pingbian-guige-guide.html | https://tools.dicomp.net/tools/optical/edge-bevel.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/sudoku-generator-guide.html | https://tools.dicomp.net/tools/fun/generator-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/wenbenquzhong-paixu-fanzhuan-guide.html | https://tools.dicomp.net/tools/it/text-dedupe-sort.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/healthcare-morse-guide.html | https://tools.dicomp.net/tools/healthcare/morse.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/laugh-generator-guide.html | https://tools.dicomp.net/tools/fun/generator-laugh.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/accounting-calc-1-guide.html | https://tools.dicomp.net/tools/accounting/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-11-guide.html | https://tools.dicomp.net/tools/dentistry/bridge-span.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/securities-calc-1-guide.html | https://tools.dicomp.net/tools/securities/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/caishuzi-1-100fanwei-guide.html | https://tools.dicomp.net/tools/fun/number-guess.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-6-guide.html | https://tools.dicomp.net/tools/reproductive-medicine/ivf-statistics.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/text-compare-guide.html | https://tools.dicomp.net/tools/it/text-diff.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/electrical-power-guide.html | https://tools.dicomp.net/tools/electromagnetism/electric-power.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/convert-speed-stride-guide.html | https://tools.dicomp.net/tools/fitness/step-stride.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-blink-guide.html | https://tools.dicomp.net/tools/fun/blink-counter.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/noise-1-guide.html | https://tools.dicomp.net/tools/eco/noise-superposition.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/edu-calc-4-guide.html | https://tools.dicomp.net/tools/edu/calc-4.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/health-calc-2-guide.html | https://tools.dicomp.net/tools/health/calc-2.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/convert-ref-cite-guide.html | https://tools.dicomp.net/tools/library/citation-format.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/ranking-guide.html | https://tools.dicomp.net/tools/edu2/exam-analysis.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/slope-4-guide.html | https://tools.dicomp.net/tools/road/grade-calc.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/it-keyword-density-guide.html | https://tools.dicomp.net/tools/it/keyword-density.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/math-calc-4-guide.html | https://tools.dicomp.net/tools/math/calc-4.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/succulent-watering-guide.html | https://tools.dicomp.net/tools/gardening/reminder-cycle-succulent.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/budget-planner-guide.html | https://tools.dicomp.net/tools/funeral/funeral-budget-planner.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/distance-4-guide.html | https://tools.dicomp.net/tools/surveying/horizontal-from-slope.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/math-calc-1-guide.html | https://tools.dicomp.net/tools/life/percentage-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/construction-calc-1-guide.html | https://tools.dicomp.net/tools/construction/calc-1.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/convert-sample-guide.html | https://tools.dicomp.net/tools/audio/audio-sample-rate.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/stats-guide.html | https://tools.dicomp.net/tools/edu/essay-word-counter.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/date-diff-guide.html | https://tools.dicomp.net/tools/life/date-difference-calculator.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/convert-fps-guide.html | https://tools.dicomp.net/tools/video/video-fps.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/fitness-calc-3-guide.html | https://tools.dicomp.net/tools/fitness/calc-3.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/qiaoliang-qiaodun-zhizuo-hezai-guide.html | https://tools.dicomp.net/tools/bridge/load-calc.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/analysis-conversion-recruit-guide.html | https://tools.dicomp.net/tools/hr/recruitment-funnel.html | 2026-11-21 | 2026-12-21 | 保留期内 | 孤儿指南重定向 |
| https://tools.dicomp.net/guides/ocr-guide.html | https://tools.dicomp.net/tools/ai/index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 无对应工具的AI指南重定向至AI工具分类 |
| https://tools.dicomp.net/guides/image-classification-guide.html | https://tools.dicomp.net/tools/ai/index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 无对应工具的AI指南重定向至AI工具分类 |
| https://tools.dicomp.net/guides/sentiment-analysis-guide.html | https://tools.dicomp.net/tools/ai/index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 无对应工具的AI指南重定向至AI工具分类 |
| https://tools.dicomp.net/guides/text-summarization-guide.html | https://tools.dicomp.net/tools/ai/index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 无对应工具的AI指南重定向至AI工具分类 |
| https://tools.dicomp.net/guides/speech-to-text-guide.html | https://tools.dicomp.net/tools/ai/index.html | 2026-11-21 | 2026-12-21 | 保留期内 | 无对应工具的AI指南重定向至AI工具分类 |
| https://tools.dicomp.net/tools/fire-rescue/calc-4.html | https://tools.dicomp.net/tools/fire/extinguisher-calc.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/transport/estimate-4.html | https://tools.dicomp.net/tools/automotive/container-loading.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/film/convert-time-1.html | https://tools.dicomp.net/tools/film/editing-timecode.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/life/generator-random-1.html | https://tools.dicomp.net/tools/it/random.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/life/generator-strength.html | https://tools.dicomp.net/tools/it/password-generator.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/fluid/continuity-equation.html | https://tools.dicomp.net/tools/hydraulic/continuity-pipe.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/food/convert-concentration.html | https://tools.dicomp.net/tools/food/syrup-brix-converter.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/food/convert-19.html | https://tools.dicomp.net/tools/food/wine-alcohol-converter.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/sports/generator-random-3.html | https://tools.dicomp.net/tools/sports/yoga-pose-generator.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/generator-8.html | https://tools.dicomp.net/tools/it/qrcode.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/astronomy/convert-17.html | https://tools.dicomp.net/tools/edu/convert-1.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/energy/water-tds-evaluator.html | https://tools.dicomp.net/tools/energy/assessor-water-quality.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/construction/area.html | https://tools.dicomp.net/tools/construction/ac-size-guide.html | 2026-11-22 | 2026-12-22 | 保留期内 | 简体+繁体各 1 页 |
| https://tools.dicomp.net/guides/convert-17-guide.html | https://tools.dicomp.net/tools/edu/convert-1.html | 2026-11-22 | 2026-12-22 | 保留期内 | 合并后遗留指南 |
| https://tools.dicomp.net/guides/area-guide.html | https://tools.dicomp.net/tools/construction/ac-size-guide.html | 2026-11-22 | 2026-12-22 | 保留期内 | 合并后遗留指南 |
| https://tools.dicomp.net/guides/water-tds-evaluator-guide.html | https://tools.dicomp.net/tools/energy/assessor-water-quality.html | 2026-11-22 | 2026-12-22 | 保留期内 | 合并后遗留指南 |
| https://tools.dicomp.net/tools/it/http-response-headers.html | https://tools.dicomp.net/tools/it/http-headers.html | 2026-11-22 | 2026-12-22 | 保留期内 | 合并后旧页 |
| https://tools.dicomp.net/guides/http-response-headers-guide.html | https://tools.dicomp.net/tools/it/http-headers.html | 2026-11-22 | 2026-12-22 | 保留期内 | 合并后指南 |
| https://tools.dicomp.net/guides/generator-strength-guide.html | https://tools.dicomp.net/guides/password-generator-guide.html | 2026-11-22 | 2026-12-22 | 保留期内 | 重复指南合并 |
| https://tools.dicomp.net/guides/vaccine-reminder-guide.html | https://tools.dicomp.net/guides/reminder-vaccine-deworming-guide.html | 2026-11-22 | 2026-12-22 | 待删 | 繁体同理 |
