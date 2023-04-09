import numpy as np

def one_year_interest_rate(pv, c1, c0=0):
    """Compute the one year interest rate (discount rate)
    given the present value and the one year cash flow.
    ----------
    pv : float
        Present value
    c1 : float
        One year cash flow
    """
    # PV = C0 + C1/(1+r) + C2/(1+r)^2 + C3/(1+r)^3 + ... + Cn/(1+r)^n
    # PV = C0 + C1/(1+r)
    # r = C1/(PV - C0) - 1
    r = (c1/ (pv - c0)) - 1
    print(f"r = {r:.2f}")
    return r

def one_year_discount_factor(r):
    # Discount factor = 1 / (1 + r) < 1
    df = 1 / (1 + r)
    print(f"df = {df:.2f}")
    return df

def compounding(c0, r, n):
    """Compute the compound interest given the initial investment, the interest
    rate and the number of years.
    ----------
    c0 : float
        Initial investment
    r : float
        Interest rate
    n : int
        Number of years
    """
    # Cn = C0 * (1 + r)^n
    cn = c0 * (1 + r) ** n
    print(f"C{n} = C0 * (1 + r)^n = {cn:.2f}")
    return cn

def non_compounding(c0, r, n):
    """Compute the money at the end with non-compounding interest, 
    given the initial investment, the interest rate and the number of years.
    ----------
    c0 : float
        Initial investment
    r : float
        Interest rate
    n : int
        Number of years
    """
    cn = c0 * (1 + (r * n))
    print(f"C{n} = {cn:.2f}")
    return cn

def one_year_npv(c0, c1, r):
    """Compute the one year net present value given the initial investment, the
    one year cash flow and the interest rate.
    ----------
    c0 : float
        Initial investment
    c1 : float
        One year cash flow
    r : float
        Interest rate of alternative investments
    """
    # NPV = C0 + C1/(1+r)
    npv = c0 + (c1 / (1 + r))
    print(f"NPV = {npv:.2f},", "do it!" if npv > 0 else "don't do it!")
    return npv

def bond(c0, r, n):
    """Compute the bond value given the initial investment, the interest rate
    and the number of years.
    ----------
    c0 : float
        Initial investment
    r : float
        Interest rate
    n : int
        Number of years
    """
    # Cn = C0 * (1 + r)^n
    cn = c0 * (1 + r) ** n
    print(f"C{n} = C0 * (1 + r)^n = {cn:.2f}")
    return cn

def mortgage_payments(p, r, n):
    """Compute the mortgage payments given the principal, the interest rate and
    the number of years.
    ----------
    p : float
        Principal
    r : float
        Interest rate per period (year)
    n : int
        Number of periods (years)
    """
    # a = p * r * (1 + r)^n / (1 + r)^n - 1
    a = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
    print(f"mortgage payments per period = {a:.2f}")
    return a

def pv_annuity(a, r, n):
    """Compute the present value of an annuity given the annuity payment, the
    interest rate and the number of years.
    ----------
    a : float
        Annuity payment
    r : float
        Interest rate per period (year)
    n : int
        Number of periods (years)
    """
    # PV = a * (1 - (1 + r)^-n) / r
    pv = a * (1 - (1 + r)**-n) / r
    print(f"present value of annuity = {pv:.2f}")
    return pv

def pv_perpetuity(a, r):
    """Compute the present value of a perpetuity given the annuity payment and
    the interest rate.
    ----------
    a : float
        Annuity payment
    r : float
        Interest rate per period (year)
    """
    # PV = a / r
    pv = a / r
    print(f"present value of perpetuity = {pv:.2f}")
    return pv

def multi_year_pv(cn, n, r):
    """Compute the present value of a multi-year cash flow given the cash flow
    after n periods, the number of periods and the interest rate.
    ----------
    cn : float
        Cash flow after n periods
    n : int
        Number of periods
    r : float
        Interest rate per period (year)
    """
    # PV = Cn / (1 + r)^n
    pv = cn / (1 + r)**n
    print(f"present value of future cash flow = {pv:.2f}")
    return pv

def effective_annual_rate(sair, n):
    """Compute the effective annual rate given the simple, quoted annual interest rate
    and the number of compounding periods per year.
    ----------
    sair : float
        Stated annual interest rate
    n : int
        Number of compounding periods per year
    """
    # EAR = (1 + sair/n)^n - 1
    ear = (1 + sair/n)**n - 1
    print(f"effective annual rate = {ear:.2f}")
    return ear

def periodic_rate(r, n):
    """Compute the periodic rate given the simple, quoted annual interest rate
    and the number of compounding periods per year.
    ----------
    r : float
        Stated annual interest rate
    n : int
        Number of compounding periods per year
    """
    # pr = r/n
    pr = r/n
    print(f"periodic rate = {pr:.2f}")
    return pr

def ear_from_periodic_rate(pr, n):
    """"Compute the effective annual rate given the periodic rate pr = sair / n 
    and the number of compounding periods per year.
    ----------
    pr : float
        Periodic interest rate
    n : int
        Number of compounding periods per year
    """
    # EAR = (1 + pr)^n - 1
    ear = (1 + pr)**n - 1
    print(f"effective annual rate = {ear:.2f}")
    return ear

def zero_coupon_bond_annual_return(f, p0):
    """Compute the annual return of a zero coupon bond given the face value and
    the price.
    ----------
    f : float
        Face value (final payment)
    p0 : float
        Price
    """
    # r = (f / p0) - 1
    r = (f / p0) - 1
    print(f"annual return = {r:.2f}")
    return r

def zero_coupon_bond_ytm(f, p0, tm):
    """Compute the yield to maturity of a zero coupon bond given the face value,
    the price and the time to maturity.
    ----------
    f : float
        Face value (final payment)
    p0 : float
        Price
    tm : float
        Time to maturity
    """
    # r = (f / p0)^(1/tm) - 1
    r = (f / p0)**(1/tm) - 1
    print(f"yield to maturity = {r:.4f}")
    return r

def zero_coupon_bond_hpr(f, p0, tm):
    """Compute the holding period return of a zero coupon bond given the face value,
    the price and the time to maturity.
    Same as yield to maturity if the bond is held to maturity 
    or ytm stays constant.
    Same as annual return.
    ----------
    f : float
        Face value (final payment)
    p0 : float
        Price
    tm : float
        Time to maturity
    """
    # r = (f / p0)^(1/tm) - 1
    r = (f / p0)**(1/tm) - 1
    print(f"holding period return = {r:.4f}")
    return r

def coupon_bond_ytm(c, f, p0, tm):
    """Compute the yield to maturity of a coupon bond given the coupon payment,
    the face value, the price and the time to maturity.
    ----------
    c : float
        Coupon payment
    f : float
        Face value (final payment)
    p0 : float
        Price
    tm : float
        Time to maturity
    """
    # r = (c + f / p0)^(1/tm) - 1
    r = (c + f / p0)**(1/tm) - 1
    print(f"yield to maturity = {r:.4f}")
    return r

def zero_coupon_bond_hpr_middle(f, p0, tm, th, ytm_sold):
    """Compute the holding period return of a zero coupon bond if it is sold before maturity.
    ----------
    f : float
        Face value (final payment)
    p0 : float
        Price
    tm : float
        Time to maturity
    th : float
        Time sold (years bond was held)
    ytm_sold : float
        Yield to maturity at time sold (and for remaining time to maturity)
    """
    # yield to maturity at time of buying
    ytm0 = (f / p0)**(1/tm) - 1
    # time left to maturity
    t_left = tm - th 
    # present value of price at time of sale
    vt = f / (1 + ytm_sold)**t_left
    # holding period return
    hpr = (vt / p0)**(1/th) - 1
    print(f"holding period return = {hpr:.4f}")
    print(f'YTM {ytm0:.4f} -> {ytm_sold:.4f} after {th:.2f} years')
    return hpr

def semi_annual_bond_price(cr, f, ytm, tm):
    """Compute the price of a semi-annual coupon bond given the coupon payment,
    the face value, the yield to maturity and the time to maturity.
    ----------
    cr : float
        Coupon rate (coupon rate = coupon payment / par value)
    f : float
        Face (par) value (final payment)
    ytm : float
        Yield to maturity
    tm : float
        Time to maturity
    """
    # Bond sells at par when coupon rate equals YTM 
    if cr == ytm:
        print(f"Bond sells at par (price = face value) = {f:.2f}")
        return f
    # Bond sells at a discount when coupon rate is less than YTM
    # --------------------
    # method 1: take twice the years
    # annual coupon payments
    ca = cr * f
    # semi-annual coupon payments
    csa = ca / 2
    # method 1: take twice the years
    p0 = 0
    # periodic rate
    pr = ytm / 2
    # coupon payments
    for i in range(1, int(tm*2)+1):
        p0 += csa / (1 + pr)**i
    # final payment
    p0 += f / (1 + pr)**(int(tm*2))
    # --------------------
    # same as
    p0_formula = coupon_bond_price(ca=csa, f=f, ytm=pr, tm=tm*2)
    # --------------------
    # method 2: use EAR
    # YTM is not an EAR, it is a SAIR
    # EAR = (1 + SAIR/2)^2 - 1
    ytm_ear = (1 + pr)**2 - 1
    p0_ear = 0
    # coupon payments, semi-annual
    for i in np.arange(0.5, tm+0.5, 0.5):
        p0_ear += csa / (1 + ytm_ear)**i
    # final payment
    p0_ear += f / (1 + ytm_ear)**tm
    # --------------------
    # not the same as
    p0_ear_formula = coupon_bond_price(ca=csa, f=f, ytm=ytm_ear, tm=tm)
    # --------------------
    print(f"price = {p0:.2f} (method 1)")
    print(f"price = {p0_ear:.2f} (method 2)")
    return p0

def coupon_bond_price(ca, f, ytm, tm):
    """Compute the price of a coupon bond given the annual coupons,
    the face value, the yield to maturity and the time to maturity.
    ----------
    ca : float
        Coupons (coupon rate = coupon payment / par value)
    f : float
        Face (par) value (final payment)
    ytm : float
        Yield to maturity
    tm : float
        Time to maturity
    """
    # Bond sells at par when coupon rate equals YTM 
    # Bond sells at a discount when coupon rate is less than YTM
    # --------------------
    # annual coupon payments
    fdr = 1 / (1 + ytm)**tm # final discount rate
    p0 = (f * fdr) + (ca / ytm) * (1 - fdr)
    print(f'price = {p0:.2f}')
    return p0

def pv_growing_perpetuity(c, g, r):
    """Compute the present value of a growing perpetuity given the annual coupon,
    the annual growth rate and the discount rate.
    ----------
    c : float
        Annual coupon
    g : float
        Annual growth rate
    r : float
        Discount rate
    """
    # pv = c / (r - g)
    pv = c / (r - g)
    print(f"present value = {pv:.2f}")
    return pv