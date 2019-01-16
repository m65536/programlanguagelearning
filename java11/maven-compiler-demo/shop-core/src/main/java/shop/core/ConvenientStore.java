package shop.core;

import shop.api.Store;
import shop.name.ShopIndex;

import javax.swing.*;


/**
 * @author Mincong Huang
 * @since 1.0
 */
public class ConvenientStore implements Store, ShopIndex {

    @Override
    public String getName() {
        Timer timer = null;
        return "Convenient Store";
    }

    @Override
    public String getAddress() {
        return "Somewhere in Paris";
    }
}
