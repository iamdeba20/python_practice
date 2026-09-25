from decimal import Decimal
name="alice"
age=20
print(f"my name is:{name} and age is:{age}")#my name is:alice and age is:20
print(f"{17.4899:.2f}")#17.49
print(f"{10:d}")#10
print(f"{68:c}{65:c}")#DA
print(f"{"hello":s}{10}")#hello10
print(f"{10000000.0:.3f}")#10000000.000
print(f"{Decimal('10000000000.0'):.3e}")#1.000e+10
print(f"{Decimal('10000000000.0'):.3E}")#1.000E+10
print(f"[{27:10d}]")#[        27]
print(f"[{'hello':10}]")#[hello     ]
print(f"[{10.430:20f}]")#[           10.430000]
print(f"[{27:<10d}]")#[27        ]
print(f"[{'hello':>10}]")#[     hello]
print(f"[{12:^7d}]")#[  12   ]
print(f"{20:d}\n{20:d}\n{-20:d}")
print(f"{12345678:,d}")#12,345,678