import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import translationEN from './locales/en.json';
import translationFR from './locales/fr.json';

const resources = {
  en: { translation: translationEN },
  fr: { translation: translationFR }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en', // default language
    fallbackLng: 'en', // fallback language if translation is missing
    keySeparator: false,
    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

export default i18n;
