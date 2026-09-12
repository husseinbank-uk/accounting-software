# Chart of Accounts - Iraqi Standard
# Format: (account_code, account_name_en, account_name_ar, account_type)

CHART_OF_ACCOUNTS = [
    # Assets (1)
    ("1", "Assets", "الاصول", "Asset"),
    
    # Non-current Assets (11)
    ("11", "Non-current Assets", "الاصول غير المتداولة", "Asset"),
    ("111", "Property, Plant and Equipment (PPE)", "الممتلكات والالات والمعدات", "Asset"),
    ("1111", "Land", "أراضي", "Asset"),
    ("1112", "Buildings, Constructions and Roads", "مباني وإنشاءات وطرق", "Asset"),
    ("1113", "Machinery and Equipment", "الات ومعدات", "Asset"),
    ("1114", "Transportation Means", "وسائط نقل وانتقال", "Asset"),
    ("1115", "Tools and Molds", "عدد وقوالب", "Asset"),
    ("1116", "Furniture and Office Equipment", "أثاث وأجهزة مكاتب", "Asset"),
    ("11161", "Furniture", "أثاث", "Asset"),
    ("11162", "Air Conditioning and Cooling Equipment", "أجهزة تكييف وتبريد", "Asset"),
    ("11163", "Computers", "حاسبات الكترونية", "Asset"),
    ("11164", "Calculators, Typewriters and Copiers", "الات حاسبة وكاتبة واستنساخ", "Asset"),
    ("11165", "Office Tools and Devices", "أدوات وأجهزة مكاتب", "Asset"),
    ("11166", "Books and Scientific References", "كتب ومراجع علمية", "Asset"),
    ("112", "Investment Properties", "العقارات الاستثمارية", "Asset"),
    ("113", "Leased Non-current Assets", "الاصول غير المتداولة المستأجرة", "Asset"),
    ("114", "Biological Assets for Display, Production and Guarding", "اصول حية لأغراض العرض والانتاج والحراسة", "Asset"),
    ("115", "Long-term Loans and Investments", "القروض والاستثمارات طويلة الاجل", "Asset"),
    ("1151", "Long-term Loans Granted", "القروض الممنوحة طويلة الاجل", "Asset"),
    ("1152", "Financial Investments", "استثمارات مالية", "Asset"),
    ("117", "Jointly Controlled Property, Plant and Equipment", "الممتلكات والالات والمعدات الخاضعة لسيطرة مشتركة", "Asset"),
    
    # Capital Expenditure (12)
    ("12", "Capital Expenditure (CapEx)", "الانفاق الرأسمالي (مشروعات تحت التنفيذ)", "Asset"),
    
    # Current Assets (13)
    ("13", "Current Assets", "الاصول المتداولة", "Asset"),
    ("131", "Inventory", "المخزون", "Asset"),
    ("132", "Accounts Receivable", "الذمم المدينة", "Asset"),
    ("1321", "Trade Receivables", "المدينون التجاريون", "Asset"),
    ("1322", "Notes Receivable", "أوراق قبض", "Asset"),
    ("1323", "Current Accounts Receivable", "حسابات جارية مدينة", "Asset"),
    ("1324", "Construction Activity Receivables", "مدينو نشاط التشييد", "Asset"),
    ("1325", "Non-current Activity Receivables", "مدينو النشاط غير الجاري", "Asset"),
    ("1326", "Miscellaneous Receivables", "حسابات مدينة متنوعة", "Asset"),
    ("13261", "Deposits with Third Parties", "تأمينات لدى الغير", "Asset"),
    ("13262", "Accrued Revenues", "إيرادات مستحقة", "Asset"),
    ("13263", "Prepaid Expenses", "مصاريف مدفوعة مقدما", "Asset"),
    ("1327", "Advances", "سلف", "Asset"),
    ("134", "Cash", "النقود", "Asset"),
    ("1341", "Cash on Hand", "نقدية بالصندوق", "Asset"),
    ("1342", "Cash at Banks", "نقدية لدى المصارف", "Asset"),
    ("1343", "Cash in Safes", "نقدية لدى الخزائن", "Asset"),
    ("1344", "Checks and Transfers", "صكوك وحوالات", "Asset"),
    ("135", "Short-term Loans and Investments", "القروض والاستثمارات قصيرة الاجل", "Asset"),
    ("1351", "Short-term Loans Granted", "قروض ممنوحة قصيرة الاجل", "Asset"),
    ("1352", "Investments in Shares, Bonds and Commercial Papers", "الاستثمارات في الاسهم والسندات والاوراق التجارية", "Asset"),
    
    # Other Assets (14)
    ("14", "Other Assets", "الاصول الاخرى", "Asset"),
    ("141", "Deferred Tax Assets", "أصول ضريبية مؤجلة", "Asset"),
    ("142", "Deferred Compensation and Penalties", "تعويضات وغرامات مؤجلة", "Asset"),
    
    # Intangible Assets (15)
    ("15", "Intangible Assets", "الاصول غير الملموسة", "Asset"),
    ("151", "Goodwill", "شهرة المحل", "Asset"),
    ("152", "Patents", "حقوق اختراع", "Asset"),
    ("153", "Franchises and Licenses", "حقوق الامتياز والتراخيص", "Asset"),
    ("154", "Trademarks", "العلامة التجارية", "Asset"),
    ("155", "Research and Experiments", "الابحاث والتجارب", "Asset"),
    ("156", "Copyrights", "حقوق النشر والطبع والتأليف", "Asset"),
    ("157", "Rights under Long-term Lease Contracts", "حقوق عقود التأجير طويلة الاجل", "Asset"),
    ("158", "Other Intangible Assets", "أصول غير ملموسة أخرى", "Asset"),
    
    # Deferred Regulatory Accounts (18)
    ("18", "Deferred Regulatory Accounts (Debit Balances)", "الارصدة المدينة لحسابات التأجيل التنظيمية", "Asset"),
    
    # Contra Accounts (19)
    ("19", "Contra Accounts (Debit Side)", "الحسابات المتقابلة المدينة", "Asset"),
    
    # Liabilities and Equity (2)
    ("2", "Liabilities and Equity", "الالتزامات وحقوق الملكية", "Liability"),
    
    # Non-current Liabilities (21)
    ("21", "Non-current Liabilities", "الالتزامات غير المتداولة", "Liability"),
    ("213", "Lease Financing Obligations", "التزامات تمويل عقود الايجار", "Liability"),
    ("215", "Long-term Liabilities", "التزامات طويلة الاجل", "Liability"),
    ("2151", "Long-term Loans Received", "قروض مستلمة طويلة الاجل", "Liability"),
    
    # Accumulated Depreciation and Allowances (22)
    ("22", "Accumulated Depreciation and Allowance for Doubtful Debts", "متراكم الاندثار والديون المشكوك في تحصيلها", "Liability"),
    ("221", "Accumulated Depreciation – PPE", "متراكم اندثار الممتلكات والالات والمعدات", "Liability"),
    ("2212", "Accumulated Depreciation – Buildings, Constructions and Roads", "متراكم الاندثار مباني وإنشاءات وطرق", "Liability"),
    ("2213", "Accumulated Depreciation – Machinery and Equipment", "متراكم اندثار الات ومعدات", "Liability"),
    ("2214", "Accumulated Depreciation – Vehicles and Transport", "متراكم اندثار وسائط نقل وانتقال", "Liability"),
    ("2215", "Accumulated Depreciation – Tools and Molds", "متراكم اندثار عدد وقوالب", "Liability"),
    ("2216", "Accumulated Depreciation – Furniture and Office Equipment", "متراكم اندثار أثاث وأجهزة مكاتب", "Liability"),
    ("222", "Accumulated Depreciation – Investment Properties", "متراكم اندثار العقارات الاستثمارية (أصول بغرض الايجار)", "Liability"),
    ("223", "Accumulated Depreciation – Finance Lease Assets", "متراكم اندثار الاصول غير المتداولة المستأجرة (ايجار تمويلي)", "Liability"),
    ("224", "Allowance for Doubtful Debts", "متراكم الديون المشكوك في تحصيلها", "Liability"),
    ("226", "Accumulated Amortization – Intangible Assets", "متراكم إطفاء الاصول غير الملموسة", "Liability"),
    ("227", "Accumulated Depreciation – Jointly Controlled PPE", "متراكم اندثار الممتلكات والالات والمعدات الخاضعة لسيطرة مشتركة", "Liability"),
    
    # Current Liabilities (23)
    ("23", "Current Liabilities", "الالتزامات المتداولة", "Liability"),
    ("232", "Accounts Payable", "الذمم الدائنة", "Liability"),
    ("2321", "Trade Payables", "دائنون تجاريون", "Liability"),
    ("2322", "Notes Payable", "أوراق دفع", "Liability"),
    ("2323", "Current Accounts Payable", "حسابات جارية دائنة", "Liability"),
    ("2324", "Commitment Accounts", "حسابات التعهدات", "Liability"),
    ("2325", "Non-current Activity Payables", "دائنو نشاط غير جاري", "Liability"),
    ("2326", "Miscellaneous Payables", "حسابات دائنة متنوعة", "Liability"),
    ("23261", "Deposits Received and Postal Accounts", "تأمينات مستلمة وحسابات التوفير والبريد", "Liability"),
    ("23262", "Unearned Revenues (Deferred Income)", "إيرادات مستلمة مقدما", "Liability"),
    ("23263", "Accrued Expenses", "مصاريف مستحقة", "Liability"),
    ("23264", "Accrued Salaries and Wages", "رواتب وأجور مستحقة", "Liability"),
    ("2327", "Deductions for Third Parties", "استقطاعات لحساب الغير", "Liability"),
    ("2328", "Dividend Payables", "دائنو توزيع الارباح", "Liability"),
    ("234", "Bank Overdrafts", "المصارف الدائنة (جاري مكشوف)", "Liability"),
    ("235", "Short-term Liabilities", "الالتزامات قصيرة الاجل", "Liability"),
    ("2351", "Short-term Loans Received", "قروض مستلمة قصيرة الاجل", "Liability"),
    
    # Other Liabilities (24)
    ("24", "Other Liabilities", "الالتزامات الاخرى", "Liability"),
    ("241", "Deferred Tax Liabilities", "التزامات ضريبية مؤجلة", "Liability"),
    ("242", "Deferred Liabilities, Claims and Penalties", "التزامات ومطالبات وغرامات مؤجلة", "Liability"),
    ("244", "Deferred Revenues", "إيرادات مؤجلة", "Liability"),
    ("245", "Lease Obligations", "التزامات عقود الايجار", "Liability"),
    ("247", "Obligation for Right-of-Use of Intangible Assets", "التزام حق استخدام الاصول غير الملموسة", "Liability"),
    
    # Provisions (25)
    ("25", "Provisions", "التخصيصات", "Liability"),
    ("258", "Miscellaneous Provisions", "مخصصات متنوعة", "Liability"),
    ("2585", "Provision for Income Tax", "مخصص ضريبة الدخل", "Liability"),
    
    # Equity (26)
    ("26", "Equity", "حقوق الملكية", "Equity"),
    ("261", "Capital", "رأس المال", "Equity"),
    ("262", "Additional Paid-in Capital (Reserves)", "رأس المال الاضافي (الاحتياطيات)", "Equity"),
    ("263", "Retained Earnings", "الارباح المحتجزة", "Equity"),
    ("2631", "Accumulated Surplus", "الفائض المتراكم", "Equity"),
    ("2632", "Accumulated Deficit", "العجز المتراكم", "Equity"),
    ("264", "Other Comprehensive Income (OCI)", "الدخل الشامل الاخر", "Equity"),
    ("269", "Current Activity Account", "حساب النشاط الجاري", "Equity"),
    ("2691", "Current Activity", "النشاط الجاري", "Equity"),
    
    # Deferred Regulatory Accounts (28)
    ("28", "Deferred Regulatory Accounts", "الحسابات التنظيمية المؤجلة", "Equity"),
    
    # Contra Credit Accounts (29)
    ("29", "Contra Credit Accounts", "الحسابات المتقابلة الدائنة", "Equity"),
    
    # Expenses (3)
    ("3", "Uses / Expenses", "الاستخدامات", "Expense"),
    
    # Salaries and Wages (31)
    ("31", "Salaries and Wages", "رواتب وأجور", "Expense"),
    ("311", "Cash Salaries – Employees", "الرواتب النقدية للموظفين", "Expense"),
    ("3111", "Salaries", "رواتب", "Expense"),
    ("3112", "Qualification Allowances", "مخصصات الشهادة", "Expense"),
    ("3113", "Position Allowances", "مخصصات المنصب", "Expense"),
    ("3114", "Family Allowances", "مخصصات عائلية", "Expense"),
    ("3115", "Professional and Technical Allowances", "مخصصات مهنية وفنية", "Expense"),
    ("3116", "Overtime Wages", "أجور أعمال إضافية", "Expense"),
    ("3117", "Compensatory Allowances", "مخصصات تعويضية", "Expense"),
    ("3118", "Incentive Bonuses and Production Rewards", "مكافآت تشجيعية وحوافز الانتاج", "Expense"),
    ("3119", "Other Allowances", "مخصصات أخرى", "Expense"),
    ("312", "Cash Wages – Workers", "الاجور النقدية للعمال", "Expense"),
    ("3121", "Wages", "أجور", "Expense"),
    ("313", "Salaries, Wages and Allowances – Non-Iraqis", "رواتب وأجور ومخصصات غير العراقيين", "Expense"),
    ("314", "Social Security Contributions – Employees", "المساهمة في الضمان الاجتماعي للموظفين", "Expense"),
    ("315", "Social Security Contributions – Workers", "المساهمة في الضمان الاجتماعي للعمال", "Expense"),
    ("316", "Social Security Contributions – Non-Iraqis", "المساهمة في الضمان الاجتماعي لغير العراقيين", "Expense"),
    ("318", "Employee Benefits", "منافع الموظفين", "Expense"),
    
    # Commodity Supplies (32)
    ("32", "Commodity Supplies", "المستلزمات السلعية", "Expense"),
    ("321", "Raw Materials and Primary Inputs", "الخامات والمواد الاولية", "Expense"),
    ("322", "Fuel and Oils", "الوقود والزيوت", "Expense"),
    ("323", "Spare Parts", "الادوات الاحتياطية", "Expense"),
    ("324", "Packaging Materials", "مواد التعبئة والتغليف", "Expense"),
    ("325", "Miscellaneous Supplies", "المتنوعات", "Expense"),
    ("326", "Employee Supplies", "تجهيزات للعاملين", "Expense"),
    ("327", "Water and Electricity", "المياه والكهرباء", "Expense"),
    ("3271", "Water", "المياه", "Expense"),
    ("3272", "Electricity", "الكهرباء", "Expense"),
    ("329", "Other Commodity Supplies", "مستلزمات سلعية أخرى", "Expense"),
    
    # Service Supplies / Operating Expenses (33)
    ("33", "Service Supplies / Operating Expenses", "المستلزمات الخدمية", "Expense"),
    ("331", "Basic Service Expenses", "نفقات الخدمات الاساسية", "Expense"),
    ("3311", "Transportation, Travel and Communication Expenses", "نفقات النقل والايفاد واتصالات", "Expense"),
    ("3312", "Healthcare Expenses", "النفقات الصحية", "Expense"),
    ("3313", "Communication Expenses", "نفقات الاتصالات", "Expense"),
    ("3314", "Research and Consulting Services", "خدمات ابحاث واستشارات", "Expense"),
    ("3315", "Training and Development Expenses", "نفقات التدريب والتطوير", "Expense"),
    ("3316", "Promotion and Hospitality Services", "خدمات الترويج والضيافة", "Expense"),
    ("332", "Maintenance Expenses", "نفقات الصيانة", "Expense"),
    ("3321", "Maintenance of Property, Plant and Equipment (PPE)", "صيانة الممتلكات والالات والمعدات", "Expense"),
    ("334", "Leasing of Non-current Assets", "استئجار اصول غير متداولة", "Expense"),
    ("3341", "Leasing of Property, Plant and Equipment (PPE)", "استئجار الممتلكات والالات والمعدات", "Expense"),
    ("335", "Losses on Financial Investments and Foreign Exchange Differences", "خسائر الاستثمارات المالية وفروقات اسعار الصرف الاجنبي", "Expense"),
    ("336", "Miscellaneous Service Expenses", "مصروفات خدمية متنوعة", "Expense"),
    ("337", "Interest Income", "فوائد مدينة", "Expense"),
    ("339", "Other Operating Expenses", "مصروفات تشغيلية أخرى", "Expense"),
    
    # Subcontracts and Operating Services (34)
    ("34", "Subcontracts and Operating Services", "المقاولات الثانوية وخدمات التشغيل", "Expense"),
    ("341", "Subcontracts", "مقاولات ثانوية", "Expense"),
    ("342", "Operating Services", "خدمات التشغيل", "Expense"),
    
    # Purchases of Goods and Land for Sale (35)
    ("35", "Purchases of Goods and Land for Sale", "مشتريات البضائع والاراضي بغرض البيع", "Expense"),
    ("351", "Purchases of Goods for Sale", "مشتريات البضائع بغرض البيع", "Expense"),
    ("352", "Purchases of Land for Sale", "مشتريات الاراضي بغرض البيع", "Expense"),
    ("353", "Purchase Returns and Allowances", "مردودات ومسموحات المشتريات", "Expense"),
    
    # Cost of Production and Goods Sold (36)
    ("36", "Cost of Production and Goods Sold", "كلف الانتاج والبضائع المباعة", "Expense"),
    ("361", "Production Cost", "كلفة الانتاج", "Expense"),
    ("362", "Cost of Goods Sold – Manufacturing", "كلف البضائع المباعة للانتاج السلعي", "Expense"),
    ("363", "Cost of Goods Sold – Trading Activity", "كلف البضائع المباعة للنشاط التجاري", "Expense"),
    
    # Depreciation and Amortization (37)
    ("37", "Depreciation and Amortization", "الاندثارات والاطفاءات", "Expense"),
    ("371", "Depreciation", "الاندثارات", "Expense"),
    ("3711", "Depreciation of Property, Plant and Equipment (PPE)", "اندثار الممتلكات والالات والمعدات", "Expense"),
    ("3712", "Depreciation of Investment Properties (Held for Rental)", "اندثار العقارات الاستثمارية (أصول بغرض الايجار)", "Expense"),
    ("3713", "Depreciation of Leased Non-current Assets (Finance Lease)", "اندثار الاصول غير المتداولة المستأجرة (ايجار تمويلي)", "Expense"),
    ("3717", "Depreciation of Jointly Controlled PPE", "اندثار الممتلكات والالات والمعدات الخاضعة لسيطرة مشتركة", "Expense"),
    ("372", "Depreciation and Amortization", "الاهلاكات والاطفاءات", "Expense"),
    ("3721", "Depreciation of Biological Assets for Display, Production and Guarding", "اهلاك اصول حية لأغراض العرض والانتاج والحراسة", "Expense"),
    ("3722", "Amortization of Intangible Assets", "إطفاء الاصول غير الملموسة", "Expense"),
    
    # Transfer Expenses (38)
    ("38", "Transfer Expenses", "المصروفات التحويلية", "Expense"),
    ("381", "Contribution to Parent or Subsidiary Expenses", "المساهمة في نفقات الوحدة الاقتصادية الرئيسة أو التابعة", "Expense"),
    ("382", "Miscellaneous Transfer Expenses", "مصروفات تحويلية متنوعة", "Expense"),
    ("384", "Taxes and Fees", "ضرائب ورسوم", "Expense"),
    ("3841", "Income Tax", "ضريبة دخل", "Expense"),
    ("385", "Subsidies / Grants", "اعانات", "Expense"),
    ("39", "Other Expenses and Losses", "المصروفات والخسائر الاخرى", "Expense"),
    ("391", "Capital Losses", "الخسائر الرأسمالية", "Expense"),
    ("392", "Incidental Expenses", "مصروفات عرضية", "Expense"),
    
    # Revenue (4)
    ("4", "Revenues", "الموارد", "Revenue"),
    
    # Revenue from commodity activity (41)
    ("41", "Revenue from commodity activity", "إيراد النشاط السلعي", "Revenue"),
    ("411", "Revenue from Extractive Industries", "إيراد نشاط الصناعات الاستخراجية", "Revenue"),
    ("412", "Revenue from Manufacturing Industries", "إيراد نشاط الصناعات التحويلية", "Revenue"),
    ("413", "Revenue from Construction Activity", "إيراد نشاط التشييد", "Revenue"),
    ("414", "Revenue from Agricultural Production (Crops)", "إيراد نشاط الانتاج النباتي", "Revenue"),
    ("415", "Revenue from Livestock Production", "إيراد نشاط الانتاج الحيواني", "Revenue"),
    ("416", "Revenue from Water and Electricity", "إيراد ماء وكهرباء", "Revenue"),
    ("417", "Revenue from Sale of Waste and By-products", "إيراد بيع المخلفات والمنتجات العرضية", "Revenue"),
    
    # Revenue from Trading Activity (42)
    ("42", "Revenue from Trading Activity", "إيراد النشاط التجاري", "Revenue"),
    ("421", "Revenue from Sales of Goods and Land for Sale", "ايراد مبيعات بضائع وأراضي بغرض البيع", "Revenue"),
    ("4211", "Revenue from Sales of Goods for Sale", "ايراد مبيعات بضائع بغرض البيع", "Revenue"),
    ("4212", "Revenue from Sales of Land for Sale", "ايراد مبيعات أراضي بغرض البيع", "Revenue"),
    ("423", "Commission Income", "عمولة مستلمة", "Revenue"),
    ("424", "Revenue from Hospitality and Tourism", "إيراد الفندقة والسياحة", "Revenue"),
    ("425", "Miscellaneous Revenues", "إيرادات متنوعة", "Revenue"),
    
    # Revenue from Service Activity (43)
    ("43", "Revenue from Service Activity", "إيراد النشاط الخدمي", "Revenue"),
    ("431", "Revenue from Basic Services", "ايراد خدمات أساسية", "Revenue"),
    ("4311", "Revenue from Transportation Services", "إيراد خدمات النقل", "Revenue"),
    ("4312", "Revenue from Healthcare Services", "ايراد خدمات صحية", "Revenue"),
    ("4313", "Revenue from Communication Services", "إيراد خدمات الاتصالات", "Revenue"),
    ("4314", "Revenue from Consulting and Technical Services", "إيراد خدمات استشارية وفنية", "Revenue"),
    ("4315", "Revenue from Education Services", "ايراد خدمات التربية والتعليم", "Revenue"),
    ("4316", "Revenue from Promotion and Hospitality Services", "ايراد خدمات الترويج والضيافة", "Revenue"),
    ("4319", "Other Basic Revenues", "ايرادات اساسية اخرى", "Revenue"),
    ("432", "Revenue from Maintenance and Repair Services", "إيراد خدمات الصيانة والتصليح", "Revenue"),
    ("434", "Rental Income from Non-current Assets", "إيجار اصول غير المتداولة", "Revenue"),
    ("4341", "Rental Income from PPE", "ايراد ايجار الممتلكات والالات والمعدات", "Revenue"),
    ("4342", "Rental Income from Investment Properties", "ايراد ايجار العقارات الاستثمارية", "Revenue"),
    ("435", "Gains on Financial Investments and Foreign Exchange Differences", "ارباح استثمارات مالية وفروقات اسعار الصرف الاجنبي", "Revenue"),
    ("436", "Miscellaneous Service Revenues", "إيراد خدمات متنوعة", "Revenue"),
    ("437", "Interest Income", "فوائد دائنة", "Revenue"),
    ("439", "Other Operating Revenues", "إيرادات تشغيلية اخرى", "Revenue"),
    
    # Operating Revenue for Third Parties (44)
    ("44", "Operating Revenue for Third Parties", "إيراد التشغيل للغير", "Revenue"),
    ("441", "Operating Revenue for Third Parties", "إيراد التشغيل للغير", "Revenue"),
    
    # Cost of Internally Manufactured Assets (45)
    ("45", "Cost of Internally Manufactured Assets", "كلفة الاصول المصنعة داخليا", "Revenue"),
    
    # Transferred Production Costs to Inventory (46)
    ("46", "Transferred Production Costs to Inventory", "كلف الانتاج المحول الى المخازن", "Revenue"),
    ("461", "Transferred Finished Production Costs to Inventory", "كلف الانتاج التام المحول الى المخازن", "Revenue"),
    
    # Transfer Revenues (48)
    ("48", "Transfer Revenues", "الايرادات التحويلية", "Revenue"),
    ("481", "Funding Grants", "منح تمويلية", "Revenue"),
    ("482", "Miscellaneous Transfer Revenues", "إيرادات تحويلية متنوعة", "Revenue"),
    ("4821", "Donations Received", "تبرعات مستلمة", "Revenue"),
    ("4822", "Compensations and Penalties", "تعويضات وغرامات", "Revenue"),
    ("4823", "Previously Written-off Debts (Recovered)", "ديون سبق شطبها", "Revenue"),
    
    # Other Revenues and Gains (49)
    ("49", "Other Revenues and Gains", "الايرادات والمكاسب الاخرى", "Revenue"),
    ("491", "Capital Gains", "المكاسب الرأسمالية", "Revenue"),
    ("4911", "Gains on Property, Plant and Equipment (PPE)", "مكاسب الممتلكات والالات والمعدات", "Revenue"),
    ("4912", "Gains on Sale of Investment Properties (Held for Rental)", "مكاسب بيع العقارات الاستثمارية (أصول بغرض الايجار)", "Revenue"),
    ("4913", "Gains on Leased Non-current Assets (Finance Lease)", "مكاسب الاصول غير المتداولة المستأجرة (ايجار تمويلي)", "Revenue"),
    ("4914", "Gains on Biological Assets for Display, Production and Guarding", "مكاسب موجودات حية لأغراض العرض والانتاج والحراسة", "Revenue"),
    ("4915", "Gains on Sale of Financial Investments", "مكاسب بيع الاستثمارات المالية", "Revenue"),
    ("492", "Incidental Revenues", "إيرادات عرضية", "Revenue"),
]

def seed_chart_of_accounts():
    """Seed the Chart of Accounts into the database"""
    from models.account import Account
    
    for code, name_en, name_ar, account_type in CHART_OF_ACCOUNTS:
        account = Account(code, name_en, account_type, f"{name_ar}")
        try:
            account.save()
        except Exception as e:
            print(f"Note: Account {code} already exists or error: {e}")
