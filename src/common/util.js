import { Tooltip } from "@mui/material";

function formatNumber(num) {
  if (num === Math.floor(num) && num > 10) {
    return num;
  }
  return `${Math.floor(num * 10000) / 100}%`;
}

function displayWithRegexFallback(text, regex, maxChars = 20) {
  if (!text.startsWith("n:")) {
    return text;
  }
  const matches = text.match(regex);
  if (matches) {
    return `${matches[1]} (Not Translated)`;
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
  formatNumber,
};
