interface IComboValues {
  label: string;
  value: string;
}

const dataValueLabel: Array<IComboValues> = [];

const op1: IComboValues = {
  label: 'Hello',
  value: '1'
};
dataValueLabel.push(op1);

const op2: IComboValues = {
  label: 'Hello',
  value: '1'
};

dataValueLabel.push(op2);

dataValueLabel.sort((a: IComboValues, b: IComboValues) =>
  a.label.localeCompare(b.label)
);
