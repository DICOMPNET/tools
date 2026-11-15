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

## 2026-11-15 补登记：存量 29 个未登记存根（均已超 1 个月保留期）

> 来源：全站 `grep TOOLBOX-REDIRECT`（29 文件）。建存根日期取该文件首次入库日期（2026-08-25 批量迁移），
> 到期日按 +1 个月计算，全部**已超期**，状态统一记「待删（超期）」。
> 删除前须按「删除 SOP」：全站内链改写 → 删文件 → `sitemap-deadlinks.xml` 登记 → 部署 success 后 `_submit_indexnow_deadlinks.py`。

| 源 URL | 目标 URL | 建存根日期 | 到期日 | 状态 | 备注 |
|---|---|---|---|---|---|
| https://tools.dicomp.net/tools/acoustics/intensity-level.html | https://tools.dicomp.net/tools/acoustics/sound-intensity-level.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/agriculture/calc-2.html | https://tools.dicomp.net/tools/agriculture/calculator-calc-density.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/biz/text-compare.html | https://tools.dicomp.net/tools/it/text-diff.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/generator-9.html | https://tools.dicomp.net/tools/biz/barcode-generator.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/image-cropper.html | https://tools.dicomp.net/tools/image/image-crop.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/design/image-resizer.html | https://tools.dicomp.net/tools/image/image-resize.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dynamics/inelastic-collision.html | https://tools.dicomp.net/tools/dynamics/momentum-conservation.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/dynamics/period-pendulum.html | https://tools.dicomp.net/tools/science/pendulum-period.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/economics/pv-annuity.html | https://tools.dicomp.net/tools/insurance/annuity-present.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/edu/generator-4.html | https://tools.dicomp.net/tools/it/summary-generator.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/energy/electrical-power.html | https://tools.dicomp.net/tools/electromagnetism/electric-power.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/password.html | https://tools.dicomp.net/tools/life/generator-strength.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/finance/word-counter.html | https://tools.dicomp.net/tools/text/stats-1.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/fitness/calculator-calc-constitution.html | https://tools.dicomp.net/tools/healthcare/bmi-calculator.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/hr/overtime-pay-calc.html | https://tools.dicomp.net/tools/legal/overtime-pay.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/investment/annuity-pv-inv.html | https://tools.dicomp.net/tools/insurance/annuity-present.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/it/calc-2.html | https://tools.dicomp.net/tools/life/base-convert.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/math/calc-1.html | https://tools.dicomp.net/tools/life/percentage-calculator.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/mechanical/calc-1.html | https://tools.dicomp.net/tools/machinery/calc-lifespan-belt.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/medical/calculator-calc-due-date.html | https://tools.dicomp.net/tools/health/pregnancy-due-date.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/nuclear/specific-activity-from-halflife.html | https://tools.dicomp.net/tools/nuclear/specific-activity.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/optical/rayleigh-resolution.html | https://tools.dicomp.net/tools/optics/rayleigh-criterion.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/optical/snell-refraction.html | https://tools.dicomp.net/tools/glass/snell-refraction.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/pet/pet-age-converter.html | https://tools.dicomp.net/tools/pet/pet-age.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/realestate/calc-2.html | https://tools.dicomp.net/tools/finance/rental-yield-calculator.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/safety/detector-strength.html | https://tools.dicomp.net/tools/it/password-strength.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/science/factorial-calculator.html | https://tools.dicomp.net/tools/math/factorial-calc.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/science/range-calculator.html | https://tools.dicomp.net/tools/statistics/range-stat.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
| https://tools.dicomp.net/tools/statistics/variance-list.html | https://tools.dicomp.net/tools/statistics/sample-variance.html | 2026-08-25 | 2026-09-25 | 待删（超期） | 简体+繁体各 1 页 |
