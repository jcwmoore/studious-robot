from datetime import datetime
from sqlalchemy import Date, Double, String, Integer, UniqueConstraint, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Metadata(Base):
    __tablename__ = '_meta_data'

    run_date:Mapped[datetime] = mapped_column(DateTime)
    records_added:Mapped[int] = mapped_column(Integer)

class DailyStockPrice(Base):
    __tablename__ = 'daily_stock_price'

    date: Mapped[Date] = mapped_column(Date)
    symbol: Mapped[str] = mapped_column(String)
    close: Mapped[float] = mapped_column(Double)
    open: Mapped[float] = mapped_column(Double)
    high: Mapped[float] = mapped_column(Double)
    low: Mapped[float] = mapped_column(Double)
    after_hours: Mapped[float] = mapped_column(Double)
    pre_market: Mapped[float] = mapped_column(Double)
    volume: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        UniqueConstraint('date', 'symbol', name='date_symbol_unique_constraint'),
    )

    def __repr__(self) -> str:
        return f"DailyStockPrice(id={self.id!r}, symbol={self.symbol!r}, open={self.open!r}, close={self.close!r}, volume={self.volume!r}, ...)"

class MarketHoliday(Base):
    __tablename__ = 'market_holiday'
    
    date: Mapped[Date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)

    __table_args__ = (
        UniqueConstraint('date', name='date_unique_constraint'),
    )

    def __repr__(self) -> str:
        return f"MarketHoliday(id={self.id!r}, date={self.date!r}, name={self.name!r}, status={self.status!r})"

class DividendEvent(Base):
    __tablename__ = 'dividend_event'

    symbol: Mapped[str] = mapped_column(String)
    declaration_date: Mapped[Date] = mapped_column(Date)
    ex_dividend_date: Mapped[Date] = mapped_column(Date)
    record_date: Mapped[Date] = mapped_column(Date)
    pay_date: Mapped[Date] = mapped_column(Date)
    amount: Mapped[float] = mapped_column(Double)
    frequency: Mapped[int] = mapped_column(Integer)
    dividend_type: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"DividendEvent(id={self.id!r}, symbol={self.symbol!r}, declaratiion_date={self.declaration_date!r}, ex_dividend_date={self.ex_dividend_date!r}, amount={self.amount!r}, ...)"

class PositionHistory(Base):
    __tablename__ = 'position_history'

    symbol: Mapped[str] = mapped_column(String)
    quantity: Mapped[float] = mapped_column(Double)
    cost_basis: Mapped[float] = mapped_column(Double)
    date: Mapped[Date] = mapped_column(Date)
    
    __table_args__ = (
        UniqueConstraint('date', 'symbol', name='date_symbol_unique_constraint'),
    )

    def __repr__(self) -> str:
        return f"PositionHistory(id={self.id!r}, symbol={self.symbol!r}, quantity={self.quantity!r}, cost_basis={self.cost_basis!r}, date={self.date!r})"
    
class FinancialStatement(DeclarativeBase):

    id: Mapped[int] = mapped_column(primary_key=True)
    symbols: Mapped[str] = mapped_column(String)
    company_name: Mapped[str] = mapped_column(String)
    start_date: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
    filing_date: Mapped[Date] = mapped_column(Date)
    fiscal_year: Mapped[int] = mapped_column(Integer)
    timeframe: Mapped[str] = mapped_column(String)
    fiscal_period: Mapped[str] = mapped_column(String)
    
    @staticmethod
    def from_dict(d):
        return BalanceSheet(**d)

class BalanceSheet(FinancialStatement):
    __tablename__ = 'balance_sheet'

    assets: Mapped[float] = mapped_column(Double, nullable=True)
    capitalization: Mapped[float] = mapped_column(Double, nullable=True)
    commitments_and_contingencies: Mapped[float] = mapped_column(Double, nullable=True)
    current_assets: Mapped[float] = mapped_column(Double, nullable=True)
    current_liabilities: Mapped[float] = mapped_column(Double, nullable=True)
    equity: Mapped[float] = mapped_column(Double, nullable=True)
    equity_attributable_to_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    equity_attributable_to_parent: Mapped[float] = mapped_column(Double, nullable=True)
    fixed_assets: Mapped[float] = mapped_column(Double, nullable=True)
    liabilities: Mapped[float] = mapped_column(Double, nullable=True)
    liabilities_and_equity: Mapped[float] = mapped_column(Double, nullable=True)
    long_term_debt: Mapped[float] = mapped_column(Double, nullable=True)
    noncurrent_assets: Mapped[float] = mapped_column(Double, nullable=True)
    noncurrent_liabilities: Mapped[float] = mapped_column(Double, nullable=True)
    other_noncurrent_assets_of_regulated_entity: Mapped[float] = mapped_column(Double, nullable=True)
    other_noncurrent_liabilities_of_regulated_entity: Mapped[float] = mapped_column(Double, nullable=True)
    other_than_fixed_noncurrent_assets: Mapped[float] = mapped_column(Double, nullable=True)
    public_utilities_property_plant_and_equipment_net: Mapped[float] = mapped_column(Double, nullable=True)
    redeemable_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    redeemable_noncontrolling_interest_common: Mapped[float] = mapped_column(Double, nullable=True)
    redeemable_noncontrolling_interest_other: Mapped[float] = mapped_column(Double, nullable=True)
    redeemable_noncontrolling_interest_preferred: Mapped[float] = mapped_column(Double, nullable=True)
    temporary_equity: Mapped[float] = mapped_column(Double, nullable=True)
    temporary_equity_attributable_to_parent: Mapped[float] = mapped_column(Double, nullable=True)


class CashFlowStatement(FinancialStatement):
    __tablename__ = 'cash_flow_statement'
    
    exchange_gains_losses: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_continuing: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_discontinued: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_financing_activities: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_financing_activities_continuing: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_financing_activities_discontinued: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_investing_activities: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_investing_activities_continuing: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_investing_activities_discontinued: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_operating_activities: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_operating_activities_continuing: Mapped[float] = mapped_column(Double, nullable=True)
    net_cash_flow_from_operating_activities_discontinued: Mapped[float] = mapped_column(Double, nullable=True)

class ComprehensiveIncomeStatement(FinancialStatement):
    __tablename__ = 'comprehensive_income_statement'

    comprehensive_income_loss: Mapped[float] = mapped_column(Double, nullable=True)
    comprehensive_income_loss_attributable_to_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    comprehensive_income_loss_attributable_to_parent: Mapped[float] = mapped_column(Double, nullable=True)
    other_comprehensive_income_loss: Mapped[float] = mapped_column(Double, nullable=True)
    other_comprehensive_income_loss_attributable_to_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    other_comprehensive_income_loss_attributable_to_parent: Mapped[float] = mapped_column(Double, nullable=True)

class IncomeStatement(FinancialStatement):
    __tablename__ = 'income_statement'

    benefits_costs_and_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    cost_of_revenue: Mapped[float] = mapped_column(Double, nullable=True)
    cost_of_revenue_goods: Mapped[float] = mapped_column(Double, nullable=True)
    cost_of_revenue_services: Mapped[float] = mapped_column(Double, nullable=True)
    costs_and_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    extraordinary_items_of_income_expense_net_of_tax: Mapped[float] = mapped_column(Double, nullable=True)
    gain_loss_on_disposition_of_stock_in_subsidiary_or_equity_method_investee: Mapped[float] = mapped_column(Double, nullable=True)
    gain_loss_on_sale_of_previouslyunissued_stock_by_subsidiary_or_equity_investee_nonoperating_income: Mapped[float] = mapped_column(Double, nullable=True)
    gain_loss_on_sale_of_properties_net_of_tax: Mapped[float] = mapped_column(Double, nullable=True)
    grossprofit: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_before_equity_method_investments: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_continuing_operations_after_tax: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_continuing_operations_before_tax: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_discontinued_operations_net_of_tax: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_discontinued_operations_net_of_tax_adjustment_to_prior_year_gain_loss_on_disposal: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_discontinued_operations_net_of_tax_during_phase_out: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_discontinued_operations_net_of_tax_gain_loss_on_disposal: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_discontinued_operations_net_of_tax_provision_for_gain_loss_on_disposal: Mapped[float] = mapped_column(Double, nullable=True)
    income_loss_from_equity_method_investments: Mapped[float] = mapped_column(Double, nullable=True)
    income_tax_expense_benefit: Mapped[float] = mapped_column(Double, nullable=True)
    income_tax_expense_benefit_current: Mapped[float] = mapped_column(Double, nullable=True)
    income_tax_expense_benefit_deferred: Mapped[float] = mapped_column(Double, nullable=True)
    indirect_operating_and_nonoperating_costs_and_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    interest_and_debt_expense: Mapped[float] = mapped_column(Double, nullable=True)
    interest_and_dividend_income_operating: Mapped[float] = mapped_column(Double, nullable=True)
    interest_expense: Mapped[float] = mapped_column(Double, nullable=True)
    interest_expense_operating: Mapped[float] = mapped_column(Double, nullable=True)
    interest_income_expense_after_provision_for_losses: Mapped[float] = mapped_column(Double, nullable=True)
    interest_income_expense_operating_net: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_attributable_to_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_attributable_to_noncontrolling_interest_plus_preferred_stock_dividends_and_other_adjustments: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_attributable_to_nonredeemable_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_attributable_to_parent: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_attributable_to_redeemable_noncontrolling_interest: Mapped[float] = mapped_column(Double, nullable=True)
    net_income_loss_available_to_common_stockholders_basic: Mapped[float] = mapped_column(Double, nullable=True)
    noninterest_expense: Mapped[float] = mapped_column(Double, nullable=True)
    noninterest_income: Mapped[float] = mapped_column(Double, nullable=True)
    nonoperating_gains_losses: Mapped[float] = mapped_column(Double, nullable=True)
    nonoperating_income_expense: Mapped[float] = mapped_column(Double, nullable=True)
    nonoperating_income_loss_plus_interest_and_debt_expense: Mapped[float] = mapped_column(Double, nullable=True)
    nonoperating_income_loss_plus_interest_and_debt_expense_plus_income_loss_from_equity_method_investments: Mapped[float] = mapped_column(Double, nullable=True)
    operating_and_nonoperating_costs_and_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    operating_and_nonoperating_revenues: Mapped[float] = mapped_column(Double, nullable=True)
    operating_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    operating_income_loss: Mapped[float] = mapped_column(Double, nullable=True)
    other_operating_income_expenses: Mapped[float] = mapped_column(Double, nullable=True)
    participating_securities_distributed_and_undistributed_earnings_loss_basic: Mapped[float] = mapped_column(Double, nullable=True)
    preferred_stock_dividends_and_other_adjustments: Mapped[float] = mapped_column(Double, nullable=True)
    provision_for_loan_lease_and_other_losses: Mapped[float] = mapped_column(Double, nullable=True)
    revenues: Mapped[float] = mapped_column(Double, nullable=True)
    revenues_excluding_interest_and_dividends: Mapped[float] = mapped_column(Double, nullable=True)
    revenues_net_of_interest_expense: Mapped[float] = mapped_column(Double, nullable=True)
    undistributed_earnings_loss_allocated_to_participating_securities_basic: Mapped[float] = mapped_column(Double, nullable=True)
