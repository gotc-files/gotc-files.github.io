import { Tooltip } from "@mui/material";

const TIME_UNITS = [
  { multiplier: 1, symbol: "s" },
  { multiplier: 60, symbol: "m" },
  { multiplier: 60, symbol: "h" },
  { multiplier: 24, symbol: "d" },
];

function formatStat(num) {
  if (num === Math.floor(num) && num > 10) {
    return num;
  }
  return `${Math.floor(num * 10000) / 100}%`;
}

function formatNumber(num) {
  if (num === 0) return "0";
  const symbolIndex = Math.floor(Math.log(num) / Math.log(1000));
  const symbol = ["", "K", "M", "B", "T"][symbolIndex];
  return `${(num / Math.pow(1000, symbolIndex))
    .toPrecision(3)
    .replace(/\.([^0]+)0+$/, ".$1")
    .replace(/\.0+$/, "")}${symbol}`;
}

function formatTime(numSeconds) {
  let timeUnitIndex = 0;
  let numUnits = numSeconds;
  let unitMultiplier = 1;
  while (
    timeUnitIndex + 1 < TIME_UNITS.length &&
    numUnits >= TIME_UNITS[timeUnitIndex + 1].multiplier
  ) {
    timeUnitIndex += 1;
    numUnits = Math.floor(numUnits / TIME_UNITS[timeUnitIndex].multiplier);
    unitMultiplier *= TIME_UNITS[timeUnitIndex].multiplier;
  }
  const remainder = numSeconds - unitMultiplier * numUnits;
  if (remainder === 0 || timeUnitIndex === 0) {
    return `${numUnits}${TIME_UNITS[timeUnitIndex].symbol}`;
  }
  const secondaryMultiplier =
    unitMultiplier / TIME_UNITS[timeUnitIndex].multiplier;
  const numSecondaryUnits = Math.ceil(remainder / secondaryMultiplier);
  return `${numUnits}${TIME_UNITS[timeUnitIndex].symbol}${numSecondaryUnits}${
    TIME_UNITS[timeUnitIndex - 1].symbol
  }`;
}

function formatData(data, type) {
  if (type === "time") {
    return formatTime(data);
  }
  if (type === "number") {
    return formatNumber(data);
  }
  return formatStat(data);
}

function displayWithRegexFallback(text, regex, maxChars = 20) {
  if (!text.startsWith("n:")) {
    return text;
  }
  const matches = text.match(regex);
  if (matches) {
    return `${matches[1]}`;
  }
  return displayTruncated(text, maxChars);
}

function displayTruncated(text, maxChars = 20) {
  if (!text.startsWith("n:")) {
    return text;
  }
  return truncateText(text.slice(2), maxChars);
}

function truncateText(text, maxChars) {
  return text.length > maxChars ? `${text.slice(0, maxChars - 3)}...` : text;
}

function displayTextWithTooltipForTruncated(
  text,
  textToElement,
  maxChars = 20
) {
  if (!text.startsWith("n:")) {
    return textToElement(text);
  }
  const nonTranslatedText = text.slice(2);
  if (nonTranslatedText.length > maxChars) {
    return (
      <Tooltip title={nonTranslatedText}>
        {textToElement(truncateText(nonTranslatedText, 20))}
      </Tooltip>
    );
  } else {
    return textToElement(nonTranslatedText);
  }
}

export {
  displayTruncated,
  displayWithRegexFallback,
  displayTextWithTooltipForTruncated,
  formatStat,
  formatData,
};
